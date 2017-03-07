# -*- coding: utf-8 -*-
from tgmagic.helper import singleton


class PrevButton:
	_text_on_button = str()
	_level_rise = 1

	def __init__(self, label, level=1):
		self._text_on_button = label
		self._level_rise = level

	def __str__(self):
		return self._text_on_button

	def __int__(self):
		return self._level_rise

	def __float__(self):
		return self._level_rise


@singleton
class Buttons:
	list = [PrevButton]


@singleton
class ExtendNames:
	previous = 'prev'
	nested = 'nested'
	start_element = 'menu'
