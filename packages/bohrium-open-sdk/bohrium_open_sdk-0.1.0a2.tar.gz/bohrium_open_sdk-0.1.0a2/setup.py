import os

from setuptools import find_packages, setup


def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), encoding="utf-8") as f:
        long_description = f.read()
    return long_description


setup(
    name="bohrium-open-sdk",
    version="0.1.0-alpha.2",
    author="Bohrium Team",
    url="https://bohrium.dp.tech/developer",
    description="bohrium-open-sdk",
    long_description=read_file("README.md"),  # detail description for pypi
    long_description_content_type="text/markdown",  # file format
    packages=find_packages("src", exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_dir={"": "src"},  # find_packages define code directory
    package_data={
        # include .txt all of them
        "": ["*.txt"]
    },
    install_requires=[],
    python_requires=">=3.8",
    entry_points={},
)
