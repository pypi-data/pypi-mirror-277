import ctypes
from pathlib import Path

# https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives

lib_path = Path(__file__).parent / "./debugbreak.dll"
lib = ctypes.CDLL(lib_path.as_posix())

# TODO: detect when we're running code from VS Code as it will skip debugbreak then
# TODO: check platform
def __debugbreak() -> None:
    """Execute __debugbreak from C extension, triggering Visual Studio popup."""
    lib.start_debug()
