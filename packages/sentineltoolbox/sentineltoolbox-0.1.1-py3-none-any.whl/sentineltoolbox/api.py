# all function are loaded in api module instead of in sentineltoolbox/__init__.py
# to avoid to load all dependencies each time.
# For example, pip loads sentineltoolbox to extract __version__ information.
# In this case, we don't want to load all sub packages and associated dependencies

from .data.flat_data import load_dataset, open_dataset
from .data.json_data import open_json
from .data.tree_data import load_datatree, open_datatree
from .flags import create_flag_array, get_flag, update_flag
from .models.credentials import S3BucketCredentials
from .models.filename_generator import (
    AdfFileNameGenerator,
    ProductFileNameGenerator,
    detect_filename_pattern,
)

__all__: list[str] = [
    "S3BucketCredentials",
    "open_dataset",
    "open_datatree",
    "open_json",
    "load_dataset",
    "load_datatree",
    "AdfFileNameGenerator",
    "ProductFileNameGenerator",
    "detect_filename_pattern",
    "create_flag_array",
    "update_flag",
    "get_flag",
]
