#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: Songyan Zhu
# Mail: zhusy93@gmail.com
# Created Time:  2018-10-23 13:28:34
#############################################


from setuptools import setup, find_packages

setup(
	name = "sciplt",
	version = "0.0.1",
	keywords = ("scientifc plot"),
	description = "scientifc plot",
	long_description = "scientifc plot",
	license = "MIT Licence",

	url="https://github.com/soonyenju/sciplt",
	author = "Dr. Songyan Zhu",
	author_email = "zhusy93@gmail.com",

	packages = find_packages(),
	include_package_data = True,
	platforms = "any",
	install_requires=[

	]
)