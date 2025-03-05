# -*- coding: utf-8 -*-
import os
import sys
import subprocess
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py

class CustomBuildPy(build_py):
    def run(self):
        # Build C library
        clib_path = os.path.join('src', 'clib')
        current_dir = os.getcwd()
        os.chdir(clib_path)
        
        try:
            subprocess.check_call(['xmake'])
        except subprocess.CalledProcessError as e:
            print(f"Error building C library: {e}")
            sys.exit(1)
        finally:
            os.chdir(current_dir)
            
        # Run original build_py
        build_py.run(self)

setup(
    name="pylibdemo",
    version="0.1.0",
    author="funcman",
    author_email="hyq1986@gmail.com",
    description="A demo Python package with C library integration",
    long_description=open("README.md", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/funcman/pylibdemo",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    package_data={
        'pylibdemo': ['*.dll', '*.so', '*.dylib'],
    },
    cmdclass={
        'build_py': CustomBuildPy,
    },
) 