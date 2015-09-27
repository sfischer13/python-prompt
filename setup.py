#!/usr/bin/env python3

import os.path

from setuptools import find_packages
from setuptools import setup


def read(name):
    path = os.path.join(os.path.dirname(__file__), name)
    with open(path) as f:
        return f.read()


setup(
    name="prompt",
    version="0.2.0",
    author="Stefan Fischer",
    author_email="sfischer13@ymail.com",
    url="https://github.com/sfischer13/python-prompt/",
    license="MIT",
    description="This is a library for prompting input on the command line.",
    long_description=read("README.rst"),
    keywords="prompt input console terminal tty",
    install_requires=[],
    packages=find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Terminals",
        "Topic :: Utilities"
    ],
    test_suite="nose.collector",
    zip_safe=True)
