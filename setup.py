# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import app
version = '0.1.0'

setup(
    name='shopping_site',
    version=version,
    author='',
    author_email='',
    packages=[
        'app',
    ],
    include_package_data=True
    install_requires=[
        'Django>=1.6.1',
    ]
    zip_safe=False,
    scripts=['app/manage.py'],
)

