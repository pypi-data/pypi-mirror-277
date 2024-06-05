from setuptools import setup, find_packages
from os import path

work_dir = path.abspath(path.dirname(__file__))

with open(path.join(work_dir, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="AndroStats",
    version="0.1.4",
    description="Stats for andrology data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    auto_discover_packages=True,
    install_requires=[],
)
