#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []

setup(
    author='Stefan Fischer',
    author_email='sfischer13@ymail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Terminals',
        'Topic :: Utilities'
    ],
    description='Library for prompting input on the command line.',
    include_package_data=True,
    install_requires=requirements,
    keywords='prompt input console terminal tty',
    license='MIT',
    long_description=readme + '\n\n' + history,
    name='prompt',
    package_dir={'prompt': 'prompt'},
    packages=['prompt'],
    python_requires='>=3.3',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    url='https://github.com/sfischer13/python-prompt',
    version='0.4.1',
    zip_safe=False)
