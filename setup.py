#!/usr/bin/env python
from distutils.core import setup


"""
@author: tezmen
@contact: https://t.me/tezmen
@license Apache License, Version 2.0, see LICENSE file
Copyright (C) 2017
"""


def requirements():
	"""Build the requirements list for this project"""
	requirements_list = list()
	with open('requirements.txt') as pc_requirements:
		for install in pc_requirements:
			requirements_list.append(install.strip())
	return requirements_list

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
	install_requires=requirements(),
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
