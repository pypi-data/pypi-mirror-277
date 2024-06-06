from pathlib import Path

UT_DATA = Path("tests/ut/data/")


def home_path_empty() -> Path:
    """
    mocked return function to replace Path.home
    always return valid but empty directory
    """
    return Path("tests/ut/data/empty")


def home_path_sample() -> Path:
    """
    mocked return function to replace Path.home
    always return valid but empty directory
    """
    return Path("tests/ut/data/home")
