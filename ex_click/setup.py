#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from setuptools import setup


setup(
    name='hi',
    version='0.1',
    py_module=['foo'],
    install_requires=[
        'Click',
    ],
    entry_points="""
        [console_scripts]
        hi=foo:start
    """,
)
