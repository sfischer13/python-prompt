
import os.path
#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup

def read(name):
    path = os.path.join(os.path.dirname(__file__), name)
    with open(path) as f:
        return f.read()

setup(
    author='Stefan Fischer',
    author_email='sfischer13@ymail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
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
    install_requires=[],
    description='Library for prompting input on the command line.',
    include_package_data=True,
    keywords='prompt input console terminal tty',
    license='MIT',
    long_description=read('README.rst'),
    name='prompt',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    python_requires='>=3.3',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    url='https://github.com/sfischer13/python-prompt',
    version='0.4.0',
    zip_safe=True)
