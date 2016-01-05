#!/usr/bin/python2
# coding:utf-8
"""
@version: 0.0.1
@author: livenowhy
@license: Apache Licence 
@contact: livenowhy@hotmail.com
@file: setup.py
@time: 2016/1/5 21:02
"""

from setuptools import setup, find_packages


setup(
    name='progressbar',
    version='0.1',
    description='Utility module to represent progress in the form of a progress bar.',
    url='http://github.com/liuzhangpei/progressbar',
    author='liuzhangpei',
    author_email='livenowhy@hotmail.com',
    packages=find_packages()
)