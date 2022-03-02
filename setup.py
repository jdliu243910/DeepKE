#!/usr/bin/env python
# coding: utf-8

import setuptools
import os

requirement_path = os.path.realpath("requirements.txt")
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='neuralkg',
    version='1.0.3',
    author='ZJUKG',
    author_email='xnchen2020@zju.edu.cn',
    url='https://github.com/zjukg/NeuralKG',
    description='An Open Source Library for Diverse Representation Learning of Knowledge Graphs',
    package_dir={"": "neuralkg"},
    packages=setuptools.find_packages("neuralkg"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=install_requires
)