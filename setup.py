# -*- coding: utf-8 -*-
from setuptools import setup

packages = ["gnuxlinux"]

package_data = {"": ["*"]}

install_requires = ["click>=8.1.7,<9.0.0", "rich>=13.9.4,<14.0.0", "setuptools>=75.6.0,<76.0.0"]

setup_kwargs = {
	"name": "gnuxlinux",
	"version": "0.1.0",
	"description": "gnu utilities eXtended",
	"long_description": "# gnux\ngnu utilities eXtended\n",
	"author": "alexeev-prog",
	"author_email": "alexeev.dev@mail.ru",
	"maintainer": "None",
	"maintainer_email": "None",
	"url": "None",
	"packages": packages,
	"package_data": package_data,
	"install_requires": install_requires,
	"python_requires": ">=3.9,<4.0",
}
from build import *

build(setup_kwargs)

setup(**setup_kwargs)
