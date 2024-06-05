#!/usr/bin/env python3

from pathlib import Path

import setuptools

project_dir = Path(__file__).parent

with project_dir.joinpath("requirements.txt").open() as f:
    install_requires = f.read().strip().split("\n")

setuptools.setup(
    name="PySimultan",
    version="0.3.2",
    description="Integrate SIMULTAN into Python",
    # Allow UTF-8 characters in README with encoding argument.
    long_description=project_dir.joinpath("README.md").read_text(encoding="utf-8"),
    keywords=["python"],
    author="Max Buehler",
    url="",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    package_data={
            # This assumes your package is named "your_package_name"
            "PySimultan2": ["resources/*", "tests/*"]
        },
    # pip 9.0+ will inspect this field when installing to help users install a
    # compatible version of the library for their Python version.
    python_requires=">=3.10",
    setup_requires=["wheel"],
    # There are some peculiarities on how to include package data for source
    # distributions using setuptools. You also need to add entries for package
    # data to MANIFEST.in.
    # See https://stackoverflow.com/questions/7522250/
    include_package_data=True,
    # This is a trick to avoid duplicating dependencies between both setup.py and
    # requirements.txt.
    # requirements.txt must be included in MANIFEST.in for this to work.
    # It does not work for all types of dependencies (e.g. VCS dependencies).
    # For VCS dependencies, use pip >= 19 and the PEP 508 syntax.
    #   Example: 'requests @ git+https://github.com/requests/requests.git@branch_or_tag'
    #   See: https://github.com/pypa/pip/issues/6162
    install_requires=install_requires,
    zip_safe=False,
    license="MIT",
    license_files=["LICENSE.txt"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
