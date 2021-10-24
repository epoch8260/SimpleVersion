# -*- coding: UTF-8 -*-
"""
Copyright (c) Yuwei Jin
Created at 2021-10-24 16:45 
Written by Yuwei Jin (642281525@qq.com)
"""

from distutils.core import setup
from setuptools import find_packages, setup

setup(
    name="sv",
    version="2.0",
    description="A simplified version library for deep learning in semantic segmentation",
    author="jyw",
    repository='https://upload.pypi.org/legacy/',
    packages=find_packages(),
    classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: System :: Logging',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
        ],
    # py_modules=['config_samples', 'libs', 'modules']
)
