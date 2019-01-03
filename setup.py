#!/usr/bin/env python3
import os
from setuptools import setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="lbcapi3",
    version="1.0.0",
    packages=["lbcapi3"],
    include_package_data=True,
    license="MIT License",
    description="Make API calls to LocalBitcoins API in python3",
    author="Chidindu Ogbonna",
    url="https://github.com/6ones/lbcapi3",
    install_requires=["requests"],
)
