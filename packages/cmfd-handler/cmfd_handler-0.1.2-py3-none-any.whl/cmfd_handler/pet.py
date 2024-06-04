#!/usr/bin/env python 3.11.0
# -*-coding:utf-8 -*-
# @Author  : Shuang (Twist) Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Website: https://cv.songshgeo.com/

"""计算潜在蒸散发的脚本
"""
from __future__ import annotations

from typing import Optional

import cf_xarray.units  # 必须在 `pint_xarray` 之前导入
import numpy as np
import pint_xarray
import pyet
import xarray as xr
from hydra import main
from loguru import logger
from metpy.calc import pressure_to_height_std, relative_humidity_from_specific_humidity
from metpy.units import units
from omegaconf import DictConfig
from tqdm import tqdm

from cmfd_handler.io import ChinaMeteForcingData, check_data_dir, setup_logger
from cmfd_handler.units import dataarray_has_unit, write_attrs

# Stefan-Boltzmann 常数 (σ) = 5.67 × 10^-8 W/m^2K^4
STEFAN_BOLTZMANN = 5.67e-8


def report_versions() -> None:
    """打印版本信息"""
    print("pint-xarray:", pint_xarray.__version__)
    print("cf-xarray:", cf_xarray.__version__)


def calc_net_rad(
    srad: xr.DataArray,
    lrad: xr.DataArray,
    temp: xr.DataArray,
    albedo: float | xr.DataArray = 0.23,
) -> xr.DataArray:
    """计算净辐射"""
    # 处理单位
    if not dataarray_has_unit(srad):
        srad = srad * units("W/m^2")
    if not dataarray_has_unit(lrad):
        lrad = lrad * units("W/m^2")
    if not dataarray_has_unit(temp):
        temp = temp * units("K")
    constant = STEFAN_BOLTZMANN * units("W/m^2/K^4")
    # 计算向上的短波辐射
    sw_up = srad * albedo
    # 假设有地表温度数据，用于计算向上的长波辐射
    lw_up = constant * temp**4
    # 计算净辐射
    return (srad - sw_up) + (lrad - lw_up)


def convert_wind_speed(
    wind: xr.DataArray,
    height_from: float = 10,
    height_to: float = 2,
    z0: float = 0.1,
) -> xr.DataArray:
    """将风速转换到指定高度"""
    # 添加单位
    height_from = height_from * units("m")
    height_to = height_to * units("m")
    z0 = z0 * units("m")
    if not dataarray_has_unit(wind):
        wind = wind * units("m/s")
    return wind * np.log(height_to / z0) / np.log(height_from / z0)


# def conver_wind_speed_to2m(uz, z):
#     return uz * 4.87 / np.log(67.8 * z - 5.42)

# return xr.apply_ufunc(
#     lambda uz, z: uz * 4.87 / np.log(67.8 * z - 5.42),
#     wind_speed,
#     10
# )


def calc_relative_humidity(
    pres: xr.DataArray,
    temp: xr.DataArray,
    shum: xr.DataArray,
) -> xr.DataArray:
    """计算相对湿度"""
    # 处理单位
    if not dataarray_has_unit(pres):
        pres = pres * units("hPa")
    if not dataarray_has_unit(temp):
        temp = temp * units("K")
    if not dataarray_has_unit(shum):
        shum = shum * units("kg/kg")
    return relative_humidity_from_specific_humidity(pres, temp, shum) * 100


def calc_reference_et(
    temp: xr.DataArray,
    rh: xr.DataArray,
    wind_speed: xr.DataArray,
    net_rad: xr.DataArray,
    pressure: xr.DataArray,
) -> xr.DataArray:
    """计算参考蒸散发"""
    # 处理单位
    for da in [temp, rh, wind_speed, net_rad, pressure]:
        if not dataarray_has_unit(da):
            raise ValueError(f"{da.name} has no unit.")
    temp = temp.pint.to("degC")
    pressure = pressure.pint.to("kPa")
    net_rad = net_rad.pint.to("MJ/m^2/d")
    wind_speed = wind_speed.pint.to("m/s")
    elevation = pressure_to_height_std(pressure)

    return pyet.pm_fao56(
        tmean=temp.pint.dequantify(),
        wind=wind_speed.pint.dequantify(),
        rn=net_rad.pint.dequantify(),
        rh=rh.pint.dequantify(),
        pressure=pressure.pint.dequantify(),
        elevation=elevation,
    )


def calc_pet_from_cmfd(
    srad: xr.DataArray,
    lrad: xr.DataArray,
    wind: xr.DataArray,
    shum: xr.DataArray,
    temp: xr.DataArray,
    pres: xr.DataArray,
    albedo: float | xr.DataArray = 0.23,
) -> xr.DataArray:
    """计算潜在蒸散发"""
    # 计算净辐射
    net_rad = calc_net_rad(srad, lrad, temp, albedo)
    # 转换风速到2m
    wind = convert_wind_speed(wind, height_from=10, height_to=2)
    # 计算相对湿度
    rh = calc_relative_humidity(pres, temp, shum)
    # 计算参考蒸散发
    return calc_reference_et(temp, rh, wind, net_rad, pres)


@main(version_base=None, config_path="../config", config_name="config")
def batch_calc_pet(cfg: Optional[DictConfig] = None):
    """批量计算参考蒸散发"""
    if cfg is None:
        raise ValueError("Configuration is required.")
    CMFD = ChinaMeteForcingData(cfg.source.folder, cfg.freq)
    handler = CMFD.batch_executor()
    handler.check(check_attrs=cfg.check_attrs)
    if not handler.checked_all(check_attrs=cfg.check_attrs):
        raise ValueError("Checking not passed.")
    with tqdm(total=len(handler.dates)) as pbar:
        for date, xda in tqdm(handler.apply_ufunc(calc_pet_from_cmfd)):
            write_attrs(xda, "pet", obligatory=True, is_out_data=True)
            folder = check_data_dir(cfg.out.folder, create=True)
            output_file = folder / date.strftime(cfg.out.pattern)
            xda.to_netcdf(output_file)
            logger.info(f"{date} saved to {output_file}.")
            pbar.update()


if __name__ == "__main__":
    setup_logger()
    batch_calc_pet()
