# -*- coding: utf-8 -*-
import os
import sys
import ctypes
from pathlib import Path

# Get library path
def _get_lib_path():
    lib_dir = Path(__file__).parent
    if sys.platform == "win32":
        lib_name = "adder.dll"
    elif sys.platform == "darwin":
        lib_name = "libadder.dylib"
    else:
        lib_name = "libadder.so"
    return str(lib_dir / lib_name)

# Load dynamic library
_lib = ctypes.CDLL(_get_lib_path())
_lib.add.argtypes = [ctypes.c_int, ctypes.c_int]
_lib.add.restype = ctypes.c_int

def add_numbers(a: int, b: int) -> int:
    """Calculate the sum of two numbers using C library function add"""
    return _lib.add(a, b)

def accumulate_n_times(num: int, count: int) -> int:
    """Accumulate num for count times"""
    result = 0
    for _ in range(count):
        result = add_numbers(result, num)
    return result 