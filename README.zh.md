# PyLibDemo

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Tests](https://github.com/funcman/pylibdemo/actions/workflows/test.yml/badge.svg)](https://github.com/funcman/pylibdemo/actions/workflows/test.yml)
[![Stars](https://img.shields.io/github/stars/funcman/pylibdemo?style=flat)](https://github.com/funcman/pylibdemo/stargazers)
[![Forks](https://img.shields.io/github/forks/funcman/pylibdemo?style=flat)](https://github.com/funcman/pylibdemo/network/members)

[English](README.md) | [中文](README.zh.md)

一个Cursor编写的工程，演示如何在Python中调用C库的示例项目。该项目包含一个简单的C库，实现了整数加法功能，并提供Python接口。

## 功能特性

- C库实现的整数加法函数
- Python封装接口
- 跨平台支持（Windows、Linux、macOS）
- 使用xmake构建C库

## 安装要求

- Python 3.6+
- xmake (用于构建C库)
- C编译器 (如GCC、MSVC、Clang)

## 安装方法

```bash
pip install pylibdemo
```

## 从源码安装

1. 克隆仓库：
```bash
git clone https://github.com/funcman/pylibdemo.git
cd pylibdemo
```

2. 安装包：
```bash
pip install .
```

## 单独编译C库

如果你只想编译C库，可以执行：

```bash
cd src/clib
xmake
```

## 使用示例

```python
from pylibdemo import add_numbers, accumulate_n_times

# 使用C库的加法函数
result = add_numbers(5, 3)  # 返回 8

# 使用Python封装的累加函数
sum_result = accumulate_n_times(2, 3)  # 返回 6 (2+2+2)
```

## 许可证

MIT License 