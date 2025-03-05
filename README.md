# PyLibDemo

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Tests](https://github.com/funcman/pylibdemo/actions/workflows/test.yml/badge.svg)](https://github.com/funcman/pylibdemo/actions/workflows/test.yml)
[![Stars](https://img.shields.io/github/stars/funcman/pylibdemo?style=flat)](https://github.com/funcman/pylibdemo/stargazers)
[![Forks](https://img.shields.io/github/forks/funcman/pylibdemo?style=flat)](https://github.com/funcman/pylibdemo/network/members)

[English](README.md) | [中文](README.zh.md)

A Cursor-written project demonstrating how to call C libraries from Python. This project includes a simple C library that implements integer addition functionality and provides a Python interface.

## Features

- C library implementation of integer addition function
- Python wrapper interface
- Cross-platform support (Windows, Linux, macOS)
- Using xmake as C library build tool

## Requirements

- Python 3.6+
- xmake (for building C library)
- C compiler (GCC, MSVC, or Clang)

## Installation

```bash
pip install pylibdemo
```

## Install from Source

1. Clone the repository:
```bash
git clone https://github.com/funcman/pylibdemo.git
cd pylibdemo
```

2. Install the package:
```bash
pip install .
```

## Building C Library Separately

If you only want to build the C library:

```bash
cd src/clib
xmake
```

## Usage Example

```python
from pylibdemo import add_numbers, accumulate_n_times

# Using C library addition function
result = add_numbers(5, 3)  # returns 8

# Using Python wrapper accumulation function
sum_result = accumulate_n_times(2, 3)  # returns 6 (2+2+2)
```

## License

MIT License 