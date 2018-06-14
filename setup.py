# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="data_parse",
    version="0.0.1",
    author="Changhai Wu",
    author_email="hailxl@gmail.com",
    description="data parse for csv etc.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alex-1q84/data_parse",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
