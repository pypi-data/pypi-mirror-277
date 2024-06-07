# -*- coding: utf-8 -*-
# @Author  : isFhy
# @Email   : fhy.sdwh@gmail.com
# @File    : setup.py
# @Time    : 2024/6/7 16:02
# **********************************************

from setuptools import find_packages, setup

setup(
    name='isfhyfp',
    version='1.0.0',
    packages=find_packages(),
    author='isfhy',
    author_email='fhy.sdwh@gmail.com',
    description='个人常用函数及自定义日志类等',
    include_package_data=True,
    license='GNU GPLv3',
    zip_safe=False,
    install_requires=[
        'requests',
    ],
)
