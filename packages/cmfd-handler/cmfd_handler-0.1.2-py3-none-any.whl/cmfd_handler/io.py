#!/usr/bin/env python 3.11.0
# -*-coding:utf-8 -*-
# @Author  : Shuang (Twist) Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Website: https://cv.songshgeo.com/

"""与保存数据的文件夹进行交互
"""

import os
import random
import sys
from functools import cached_property, lru_cache
from inspect import signature
from pathlib import Path
from typing import Any, Callable, Dict, Generator, List, Literal, Optional, cast

import pandas as pd
import xarray as xr
from loguru import logger
from tqdm import tqdm

try:
    from typing import TypeAlias
except ImportError:
    from typing_extensions import TypeAlias

from cmfd_handler.units import (
    CONFIG,
    convert_rate_to_volume,
    get_expected_attrs,
    open_nc_with_unit,
)

CMFDataVar: TypeAlias = Literal[
    "srad",  # 短波辐射
    "lrad",  # 长波辐射
    "wind",  # 10米处风速（m/s）
    "shum",  # 湿度
    "temp",  # 温度
    "pres",  # 气压
    "prec",  # 降水率
    "prec_mm",  # 降水量
    "pet",  # 相对蒸散发
    "max_temp",  # 最高温度
    "min_temp",  # 最低温度
]
DataFreq: TypeAlias = Literal["D", "M", "Y"]
PathLike: TypeAlias = str | Path


def setup_logger() -> None:
    """设置日志记录器"""
    fmt = "{message}\n"
    logger.remove()
    logger.add(
        sys.stderr,
        level="INFO",
    )
    logger.add(
        "pet_ch.log",
        rotation="1 week",
        retention="10 days",
        level="DEBUG",
        format=fmt,
    )


def check_data_dir(path: Optional[PathLike] = None, create: bool = False) -> Path:
    """检查数据路径是否存在"""
    if path is None:
        return Path.cwd()
    path = Path(path)
    if not os.path.isdir(path):
        if create:
            os.makedirs(path)
            logger.warning(f"Create directory: {path}")
        else:
            raise FileNotFoundError(f"Path not found: {path}")
    return path


def check_nc_file(path: Path, var: str) -> bool:
    """检查nc文件是否存在"""
    if not path.is_file():
        raise FileNotFoundError(f"File {path} not found.")
    if ".nc" not in path.suffixes:
        logger.critical(f"{path} is NOT NetCDF file, skipped.")
        return False
    if var not in path.stem:
        logger.critical(f"{path.name}: varname {var} not found, skipped.")
        return False
    return True


def check_dataarray(path: Path, var: str) -> bool:
    """检查 DataArray 的属性"""
    # 检查变量名是否存在
    ds = xr.open_dataset(path)
    if var not in ds:
        logger.critical(f"{path.name}: var {var} not found.")
        return False
    # 检查变量的属性
    attrs = clean_vars(var)
    da = ds[var]
    for key, value in attrs.items():
        if key not in da.attrs:
            logger.warning(f"{path.name}: attribute '{key}' not found.")
            continue
        attr_value = da.attrs[key]
        if attr_value != value:
            logger.warning(
                f"Attribute '{key}' mismatch in {path.name}: expected {value},"
                f"got {attr_value}."
            )
    return True


def clean_vars(
    varname: Optional[str] = None,
    is_out_data: Optional[bool] = None,
) -> Dict[str, Dict[str, str]]:
    """清理变量名"""
    expected_vars = get_expected_attrs(is_out_data)
    if varname is None:
        return expected_vars
    if isinstance(varname, str):
        try:
            return expected_vars[varname]
        except KeyError as e:
            raise KeyError(f"Variable '{varname}' not expected.") from e
    else:
        raise TypeError(f"Unexpected type: {type(varname)}")


def unpack_vars(
    expected_dates: pd.Series,
    varname: Optional[str] = None,
    is_out_data: bool = False,
) -> pd.Series:
    """将文件名中的变量名填充好"""
    included_vars = clean_vars(varname, is_out_data).keys()
    unpacked_files = []
    for var in included_vars:
        res = expected_dates.str.replace("{var}", var, regex=False)
        res = res.reset_index(name="path", allow_duplicates=True)
        res["var"] = var
        unpacked_files.append(res)
    data = pd.concat(unpacked_files).rename({"index": "date"}, axis=1)
    return data.reset_index(drop=True)[["date", "var", "path"]]


@lru_cache
def _batch_executor(
    self,
    start: str,
    freq: DataFreq = "D",
    pattern: Optional[str] = None,
    until: Optional[str] = None,
    is_out_data: bool = False,
) -> pd.DataFrame:
    """检查批处理任务是否能正常运行。"""
    if until:
        dates = pd.date_range(start=start, end=until, freq=freq)
    else:
        dates = pd.DatetimeIndex([start])
    if pattern is None:
        pattern = CONFIG.get("pattern").get(freq)
    series = pd.Series(dates.strftime(pattern), index=dates)
    data = unpack_vars(series.drop_duplicates(), is_out_data=is_out_data)
    return BatchHandler(data, self.folder, freq)


class BatchHandler:
    """批处理任务类"""

    def __init__(
        self,
        items: pd.DataFrame,
        folder: Path,
        freq: DataFreq,
    ) -> None:
        self.items = items
        self.folder = folder
        self.freq = freq

    def __repr__(self) -> str:
        return f"<BatchHandler: {len(self.dates)} dates and {len(self.variables)} vars>"

    @cached_property
    def variables(self) -> List[str]:
        """变量列表"""
        return self.items["var"].unique().tolist()

    @cached_property
    def dates(self) -> List[str]:
        """日期列表"""
        return self.items["date"].drop_duplicates()

    @cached_property
    def _index(self) -> pd.Series:
        """索引"""
        return self.items.set_index(["date", "var"])["path"]

    def checked_all(self, check_attrs: bool = True) -> bool:
        """检查是否所有文件都存在"""
        passed = self.report_check("exist").all().all()
        if check_attrs:
            passed &= self.report_check("attrs").all().all()
        return passed

    def sel(self, var: CMFDataVar) -> pd.Series:
        """选取变量"""
        subset = self.items[self.items["var"] == var]
        return subset.set_index("date")["path"]

    def loc(self, date, var: Optional[CMFDataVar] = None) -> pd.Series | Path:
        """选取数据"""
        if var is None:
            return self._index.loc[date]
        return self._index.loc[date, var]

    def check(self, check_attrs: bool = False) -> None:
        """检查批处理任务是否能正常运行。"""

        def check_a_row(series: pd.Series, check_func: Callable):
            path = self.folder / series["path"]
            var = series["var"]
            return check_func(path=path, var=var)

        tqdm.pandas()
        logger.info("检查文件是否存在。")
        self.items["exist"] = self.items.progress_apply(
            check_a_row, axis=1, check_func=check_nc_file
        )
        if not check_attrs:
            return
        logger.info("检查属性是否匹配")
        self.items["attrs"] = self.items.progress_apply(
            check_a_row, axis=1, check_func=check_dataarray
        )

    def report_check(
        self,
        item: Literal["exist", "attrs"] = "exist",
    ) -> pd.DataFrame:
        """检查结果"""
        if item not in self.items.columns:
            raise NotImplementedError("Please call `.check()` method firstly.")
        return self.items.pivot_table(
            index="date", columns="var", values=item, aggfunc="sum"
        ).astype(bool)

    def read_data(
        self, path: PathLike, var: CMFDataVar, expected_unit: Optional[str] = None
    ) -> xr.DataArray:
        """读取 DataArray"""
        if not isinstance(path, Path):
            path = self.folder / path
        if var == "prec" and expected_unit == "mm":
            da = open_nc_with_unit(path, var)
            return convert_rate_to_volume(da, freq=self.freq)
        return open_nc_with_unit(path, var, expected_unit=expected_unit)

    def merge_data(
        self,
        var: CMFDataVar,
        date_slice: Optional[slice] = None,
        unit: Optional[str] = None,
    ) -> xr.DataArray:
        """读取并沿时间轴合并数据成为一个 DataArray。

        Parameters:
            var:
                变量名。
            date_slice:
                日期切片。
            unit:
                期望的单位。

        Returns:
            将所有满足条件的 DataArray 沿时间轴合并成一个 DataArray。
        """
        if date_slice is None:
            date_slice = slice(None)
        elif not isinstance(date_slice, slice):
            raise TypeError("`date_slice` must be a slice object.")
        paths = self.sel(var).loc[date_slice]
        dsets = [self.read_data(path, var, unit) for path in paths]
        return xr.concat(dsets, dim="time")

    def demo(
        self,
        var: CMFDataVar,
        date: str = "random",
        expected_unit: Optional[str] = None,
        mean_time: bool = True,
    ) -> xr.DataArray:
        """查看示例文件"""
        if date == "random":
            date = random.choice(self.dates)
        path = self.loc(date, var)
        logger.info(f"示例文件: {path}")
        da = self.read_data(path, var, expected_unit=expected_unit)
        if mean_time:
            return da.mean("time")
        return da

    def _apply_once(
        self,
        ufunc: Callable,
        date: str,
        expected_units: Optional[Dict[str, str]] = None,
        **kwargs,
    ) -> Any | Generator[Any, None, None]:
        if expected_units is None:
            expected_units = {}
        for sig in signature(ufunc).parameters:
            if sig in self.variables:
                path = self.loc(date=date, var=cast(CMFDataVar, sig))
                unit = expected_units.get(sig, None)
                kwargs.update({sig: self.read_data(path, cast(CMFDataVar, sig), unit)})
        return ufunc(**kwargs)

    def apply_ufunc(
        self,
        ufunc: Callable,
        date: Optional[str] = None,
        expected_units: Optional[Dict[str, str]] = None,
        **kwargs,
    ) -> Optional[Any | Generator[Any, None, None]]:
        """应用某个以气象数据为输入的函数"""
        # 如果没有指定日期，则遍历所有日期，返回一个生成器
        if date is None:
            for dt in self.dates:
                res = self._apply_once(ufunc, dt, expected_units, **kwargs)
                yield dt, res
            return None
        # 如果指定了日期，则读取该日期的数据，然后应用函数
        return self._apply_once(ufunc, date, expected_units, **kwargs)


class ChinaMeteForcingData:
    """中国气象数据类.
    中国区域地面气象要素驱动数据集，包括：
    1. 近地面气温
    2. 近地面气压
    3. 近地面空气比湿
    4. 近地面全风速
    5. 地面向下短波辐射
    6. 地面向下长波辐射
    7. 地面降水率共7个要素。
    数据为NETCDF格式，时间分辨率为3小时，水平空间分辨率为0.1°。
    可为中国区陆面过程模拟提供驱动数据。

    该数据集是以国际上现有的Princeton再分析资料、GLDAS资料、GEWEX-SRB辐射资料，以及TRMM降水资料为背景场，融合了中国气象局常规气象观测数据制作而成。详细过程请参阅参考文献。原始资料来自于气象局观测数据、再分析资料和卫星遥感数据。已去除非物理范围的值，采用ANU-Spline统计插值。精度介于气象局观测数据和卫星遥感数据之间，好于国际上已有再分析数据的精度。
    """

    def __init__(
        self,
        folder: PathLike,
        freq: DataFreq,
        start: str = "1979-01-01",
        until: Optional[str] = "2018-12-31",
    ) -> None:
        self.folder = check_data_dir(folder)
        self.freq = freq
        self.start = start
        self.until = until

    @property
    def freq(self) -> DataFreq:
        """处理的时间频率"""
        return self._freq

    @freq.setter
    def freq(self, freq: DataFreq) -> None:
        """设置时间频率"""
        if freq == "H":
            raise NotImplementedError
        if freq not in ("D", "M", "Y"):
            raise TypeError(f"Unexpected frequency '{freq}'.")
        self._freq = freq

    def info(self, verbose: bool = False) -> pd.Series:
        """显示数据集信息"""
        logger.info(f"数据集路径: {self.folder}")
        logger.info(f"时间频率: {self.freq}")
        logger.info(f"开始时间: {self.start}")
        logger.info(f"结束时间: {self.until}")
        handler = self.batch_executor()
        handler.check(check_attrs=verbose)
        return handler

    def batch_executor(
        self,
        pattern: Optional[str] = None,
        is_out_data: Optional[bool] = False,
    ) -> BatchHandler:
        """检查批处理任务是否能正常运行。"""
        return _batch_executor(
            self,
            start=self.start,
            freq=self.freq,
            pattern=pattern,
            until=self.until,
            is_out_data=is_out_data,
        )
