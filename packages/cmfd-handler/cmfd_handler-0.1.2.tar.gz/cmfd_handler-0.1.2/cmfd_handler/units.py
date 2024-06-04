#!/usr/bin/env python 3.11.0
# -*-coding:utf-8 -*-
# @Author  : Shuang (Twist) Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Website: https://cv.songshgeo.com/

"""单位转换
"""
from __future__ import annotations

import importlib.resources as pkg_resources
from pathlib import Path
from typing import TYPE_CHECKING, Dict, Optional

import pint
import xarray as xr
import yaml
from metpy.units import units
from omegaconf import OmegaConf
from pint_xarray import unit_registry as ureg

if TYPE_CHECKING:
    from cmfd_handler.io import CMFDataVar, DataFreq, PathLike


_PATH = pkg_resources.files("config") / "vars.yaml"
with open(Path(str(_PATH)), "r", encoding="utf-8") as f:
    _CONFIG: dict = yaml.safe_load(f)

CONFIG = OmegaConf.create(_CONFIG)
INPUTS: Dict[str, Dict] = CONFIG.get("vars", {})
OUT: Dict[str, Dict] = CONFIG.get("out", {})


def is_valid_unit(unit_str: str) -> bool:
    """检查单位字符串是否有效。"""
    try:
        # 尝试解析单位字符串
        ureg.parse_expression(unit_str)
        return True
    except pint.errors.UndefinedUnitError:
        # 如果解析失败，则返回 False
        return False


def convert_rate_to_volume(
    rate: xr.DataArray,
    freq: DataFreq,
) -> xr.DataArray:
    """Convert rate to volume."""
    if freq == "D":
        hours = 24 * units("hr")
    elif freq == "M":
        hours = 30 * 24 * units("hr")
    elif freq == "Y":
        hours = 365 * 24 * units("hr")
    return (rate * hours).pint.to("mm")


def dataarray_has_unit(da: xr.DataArray) -> bool:
    """检查 DataArray 是否包含单位。"""
    return isinstance(da.data, ureg.Quantity)


def get_expected_attrs(is_out_data: Optional[bool] = None) -> Dict[str, Dict]:
    """根据是否输出数据返回预期的变量名。"""
    if is_out_data is None:
        return {**OUT, **INPUTS}
    if not isinstance(is_out_data, bool):
        raise TypeError("is_out_data should be a boolean.")
    return OUT if is_out_data else INPUTS


def write_attrs(
    da: xr.DataArray,
    varname: CMFDataVar,
    is_out_data: bool = False,
    obligatory: bool = False,
) -> bool:
    """为数据撰写属性名."""
    expected_attrs = get_expected_attrs(is_out_data)
    da.name = varname
    unit = expected_attrs[varname].get("units")
    long_name = expected_attrs[varname].get("long_name")
    flag = bool(unit) and bool(long_name)
    if obligatory and not flag:
        raise ValueError(
            f"Unit {unit} and long_name {long_name} are required,"
            f"but not all satisfied for {varname}."
        )
    da.attrs["units"] = unit
    da.attrs["long_name"] = long_name
    return flag


def open_nc_with_unit(
    path: PathLike,
    varname: CMFDataVar,
    expected_unit: Optional[str] = None,
) -> xr.DataArray:
    """打开nc文件，根据变量名读取变量，添加单位，返回xarray.DataArray"""
    ds = xr.open_dataset(path)
    if varname not in ds:
        raise ValueError(f"{varname} not found.")
    da = ds[varname].pint.quantify()
    if expected_unit:
        if not is_valid_unit(expected_unit):
            raise ValueError(f"Invalid unit: {expected_unit}")
        da = da.pint.to(expected_unit)
    return da
