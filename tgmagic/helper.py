# -*- coding: utf-8 -*-


def singleton(class_):
	"""
	Function for realisation of singleton pattern
	"""
	instances = {}

	def get_instance(*args, **kwargs):
		if class_ not in instances:
			instances[class_] = class_(*args, **kwargs)
		return instances[class_]
	return get_instance


def menu(function_text):
	"""
	Decorator for plain-text handler
	:param function_text: function which set as handle in bot class
	:return:
	"""
	def wrapper(self, bot, update):
		self.text_menu(bot, update)
		function_text(self, bot, update)
	return wrapper
