#!/usr/bin/env python 3.11.0
# -*-coding:utf-8 -*-
# @Author  : Shuang (Twist) Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Website: https://cv.songshgeo.com/

"""转化降水量单位的脚本
"""

from typing import Optional

from hydra import main
from loguru import logger
from omegaconf import DictConfig
from tqdm import tqdm

from cmfd_handler.io import ChinaMeteForcingData, check_data_dir, setup_logger
from cmfd_handler.units import write_attrs


@main(version_base=None, config_path="../config", config_name="config")
def batch_convert_prec(cfg: Optional[DictConfig] = None):
    """批量计算参考蒸散发"""
    if cfg is None:
        raise ValueError("Configuration is required.")
    CMFD = ChinaMeteForcingData(cfg.source.folder, cfg.freq)
    handler = CMFD.batch_executor()
    handler.check(check_attrs=cfg.check_attrs)
    if not handler.checked_all(check_attrs=cfg.check_attrs):
        raise ValueError("Checking not passed.")
    folder = check_data_dir(cfg.out.folder, create=True)
    with tqdm(total=len(handler.dates)) as pbar:
        for date, filename in handler.sel("prec").items():
            xda = handler.read_data(
                filename, "prec", expected_unit="mm"
            ).pint.dequantify()
            output_file = folder / date.strftime(cfg.out.pattern)
            write_attrs(xda, "prec_mm", obligatory=True, is_out_data=True)
            xda.to_netcdf(output_file)
            logger.info(f"{date} saved to {output_file}.")
            pbar.update()


if __name__ == "__main__":
    setup_logger()
    batch_convert_prec()
