#!/usr/bin/env python3

import os.path

from setuptools import find_packages
from setuptools import setup

def read(name):
    path = os.path.join(os.path.dirname(__file__), name)
    with open(path) as f:
        return f.read()

setup(
    author_email='sfischer13@ymail.com',
    author='Stefan Fischer',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Terminals',
        'Topic :: Utilities'
    ],
    description='This is a library for prompting input on the command line.',
    install_requires=[],
    keywords='prompt input console terminal tty',
    license='MIT',
    long_description=read('README.rst'),
    name='prompt',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    url='https://github.com/sfischer13/python-prompt/',
    version='0.4.0',
    zip_safe=True)
