import shutil
from datetime import datetime
from pathlib import Path
from typing import Any

import numpy as np
import xarray as xr
import zarr
from datatree import DataTree

DATE_FORMAT = r"%Y%m%dT%H%M%S"


def fix_path(path: Path | None, **kwargs: Any) -> Path | None:
    if path is None:
        return None
    path = Path(path).absolute()
    if path.exists():
        force = kwargs.get("force", False)
        ask = kwargs.get("ask", False)
        if force and path.suffix not in [".zarr", ".zip"]:
            print("CANNOT FORCE OVERWRITE on path without .zarr or .zip extenstion")
            force = False
        if ask:
            force = input(f"  -> replace {path} ? [n]") == "y"
        if force:
            if path.is_dir():
                shutil.rmtree(str(path))
            elif path.is_file():
                path.unlink()
            else:
                raise NotImplementedError
            print(f"REMOVE {path}")
            return path
        else:
            print(f"KEEP existing path {path}")
            return None
    else:
        return path


def _save_on_disk(dt: DataTree[Any], **kwargs: Any) -> None:
    zarr_path = fix_path(kwargs.get("url"), **kwargs)
    zip_path = fix_path(kwargs.get("url_zip"), **kwargs)

    if zarr_path:
        print(f"CREATE {zarr_path!r}")
        dt.attrs["filename"] = zarr_path.name
        dt.to_zarr(zarr_path)

    if zip_path:
        with zarr.ZipStore(zip_path) as store:
            print(f"CREATE {zip_path!r}")
            dt.attrs["filename"] = zip_path.name
            dt.to_zarr(store)


def check_datatree_sample(dt: DataTree[Any]) -> None:
    assert "other_metadata" in dt.attrs  # nosec
    assert "measurements" in dt  # nosec
    assert "coarse" in dt["measurements"]  # nosec
    assert "fine" in dt["measurements"]  # nosec
    assert "var1" in dt["measurements/coarse"].variables  # nosec
    var1 = dt["measurements/coarse/var1"]
    assert var1.shape == (2, 3)  # nosec


def create_datatree_sample(**kwargs: Any) -> DataTree[Any]:
    data = xr.DataArray(
        np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]),
        dims=("x", "y"),
        coords={"x": [10, 20], "y": [10, 20, 30]},
    )

    ds_coarse = xr.Dataset({"var1": data})
    ds_fine: xr.Dataset = ds_coarse.interp(coords={"x": [10, 15, 20], "y": [10, 15, 20, 25, 30]})
    ds_root = xr.Dataset(attrs={"other_metadata": {}})

    dt = DataTree.from_dict({"measurements/coarse": ds_coarse, "measurements/fine": ds_fine, "/": ds_root})

    _save_on_disk(dt, **kwargs)

    return dt


def create_datatree_empty(**kwargs: Any) -> DataTree[Any]:
    dt: DataTree[Any] = DataTree(name="empty")
    _save_on_disk(dt, **kwargs)
    return dt


def create_datatree_empty_adf(
    adf_prefix: str,
    root_dir: str | None = None,
    creation_date: datetime | None = None,
    **kwargs: Any,
) -> DataTree[Any]:
    if creation_date is None:
        creation_date = datetime.now()
    date_str = creation_date.strftime(DATE_FORMAT)

    if root_dir is None:
        kwargs["url"] = None
        kwargs["url_zip"] = None
    else:
        kwargs["url"] = Path(root_dir, f"{adf_prefix}_{date_str}.zarr")
        kwargs["url_zip"] = Path(root_dir, f"{adf_prefix}_{date_str}.zip")

    dt: DataTree[Any] = DataTree(name="empty")
    dt.attrs = {"properties": {"created": date_str}}
    dt.attrs.update(kwargs.get("attrs", {}))
    _save_on_disk(dt, **kwargs)
    return dt
