#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from setuptools import setup

if sys.argv[-1] == 'setup.py':
    print('To install, run \'python setup.py install\'')
    print()

if sys.version[0] < '3':
    print("Please install with Python 3. Aborting installation.")
    sys.exit(0)

sys.path.insert(0, 'potterscript')
import release

if __name__ == "__main__":
    setup(
        name = release.name,
        version = release.__version__,
        author = release.__author__,
        author_email = release.__email__,
        description = release.__description__,
        url='https://github.com/OrkoHunter/PotterScript',
        keywords='Harry Potter Programming Language Potter Script',
        packages = ['potterscript'],
        license = 'MIT License',
        entry_points = {
            'console_scripts': [
                'potterscript = potterscript.pottershell:main',
            ]
        },
        install_requires = [],
        test_suite = 'nose.collector',
        tests_require = ['nose>=0.10.1']
    )
