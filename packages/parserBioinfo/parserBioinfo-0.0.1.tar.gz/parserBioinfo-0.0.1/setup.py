#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os 
from setuptools import setup, find_packages

def get_install_requires():
    reqs = [
            'pandas>=1.2.5',
            'openpyxl>=3.1.2',
            'numpy'
            ]
    return reqs

setup(
    name = "parserBioinfo",
    version = "0.0.1",
    author ="Guijiang",
    author_email = "guijiang_wang@163.com",
    long_description_content_type="text/markdown",
    url = 'https://github.com/xianyu-123/sqllite2excel',
    long_description = open('README.md',encoding="utf-8").read(),
    python_requires=">=3.6",
    install_requires=get_install_requires(),
    packages = find_packages(),
    license = 'Apache',
    classifiers = [
       'License :: OSI Approved :: Apache Software License',
       'Natural Language :: English',
       'Operating System :: OS Independent',
       'Programming Language :: Python',       
       'Programming Language :: Python :: 3.6',
       'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    # package_data={'': ['*.csv', '*.txt','*.sqlite','.toml']}, #这个很重要
    # include_package_data=True #也选上

)
