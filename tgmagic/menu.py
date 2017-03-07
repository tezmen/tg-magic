# -*- coding: utf-8 -*-
from telegram import KeyboardButton
import dpath.util
from tgmagic.buttons import Buttons
from tgmagic.buttons import ExtendNames
from tgmagic.helper import singleton


@singleton
class MagicMenu:
	__menu_storage = dict()
	__menu_state = dict()
	__action_storage = dict()
	__user_id = str()

	def __init__(self, menu, user_id):
		"""
		:param menu: menu dictionary
		:param user_id: telegram user id
		"""
		self.__menu_storage = menu
		self.__menu_state = '/' + ExtendNames().start_element
		self.__action_storage = str()
		self.__user_id = user_id

	def get_keyboard(self):
		"""
		Generate tg-keyboad obj list
		:return:
		"""
		user_menu = dpath.util.get(self.__menu_storage, self.__menu_state)
		keyboard = list()
		if isinstance(user_menu, str):
			prev_menu_path = str(self.__menu_state).split('/')
			del prev_menu_path[-1]
			user_menu = dpath.util.get(self.__menu_storage, '/'.join(prev_menu_path))
			self.__menu_state = '/'.join(prev_menu_path)
		for element in user_menu:
			if (type(user_menu[element]) is str) or (type(user_menu[element]) in Buttons().list):
				keyboard.append([
					KeyboardButton(str(user_menu[element])),
				])
			elif type(user_menu[element]) is tuple:
				for sub_element in user_menu[element]:
					keyboard.append([
						KeyboardButton(str(sub_element)),
					])
		return keyboard

	def set_state(self, key):
		"""
		Set current state of the menu.
		:param key:
		:return:
		"""
		current = dpath.util.get(self.__menu_storage, self.__menu_state)
		for menu in self.__find_in(current, key, by_value=True):
			for elements in menu:
				self.__action_storage = elements
				if '{0}_{1}'.format(elements, ExtendNames().nested) in current:
					self.__menu_state += '/{0}_{1}'.format(elements, ExtendNames().nested)
				else:
					if elements == ExtendNames().previous:
						if self.__menu_state != '/{}'.format(ExtendNames().start_element):
							prev_menu_path = str(self.__menu_state).split('/')
							del prev_menu_path[-1]
							self.__menu_state = '/'.join(prev_menu_path)
							return
					else:
						self.__menu_state += '/{}'.format(elements)

	def get_action(self, obj):
		"""
		Get function for callback exec
		:param obj:
		:return:
		"""
		return getattr(obj, self.__action_storage)

	def __find_in(self, obj, condition, by_value=False, path=None):
		"""
		Function for recursive search in list or dict obj by key/value
		:param obj: object to be searched.
		:param condition: data for search
		:param by_value: flag to set by value searching
		:param path:
		"""
		if path is None:
			path = []
		if isinstance(obj, list):
			for index, value in enumerate(obj):
				new_path = list(path)
				new_path.append(index)
				for result in self.__find_in(value, condition, path=new_path, by_value=by_value):
					yield result
		if isinstance(obj, dict):
			for key, value in obj.items():
				new_path = list(path)
				new_path.append(key)
				for result in self.__find_in(value, condition, path=new_path, by_value=by_value):
					yield result
				search_value = value if by_value else key
				if condition == str(search_value):
					new_path = list(path)
					new_path.append(key)
					yield new_path
