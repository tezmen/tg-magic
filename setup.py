#!/usr/bin/env python
from distutils.core import setup

"""
@author: tezmen
@contact: https://t.me/tezmen
@license Apache License, Version 2.0, see LICENSE file
Copyright (C) 2017
"""

setup(
	name='tgmagic',
	version='1.0',
	description='Module for multi-level menu in telegram bots based on "python-telegram-bot" Edit',
	author='tezmen',
	license='Apache License, Version 2.0, see LICENSE file',
	keywords='telegram, bot, keyboard, simple, multi-level, three, menu',
	author_email='tezmenpro@gmail.com',
	url='https://github.com/tezmen/tg-magic',
	packages=['tgmagic'],
	install_requires=['python-telegram-bot>=5.0', 'requests>=2.0', 'dpath=>1.4.0'],
	classifiers=[
		'License :: OSI Approved :: Apache Software License',
		'Operating System :: OS Independent',
		'Environment :: Console',
		'Development Status :: 3 - Alpha',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: Implementation :: PyPy',
		'Programming Language :: Python :: Implementation :: CPython',
	]
)
