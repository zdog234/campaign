from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("campaign")
except PackageNotFoundError:
    # package is not installed
    pass
