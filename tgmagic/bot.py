# -*- coding: utf-8 -*-
from telegram import ReplyKeyboardMarkup
from tgmagic.menu import MagicMenu
from collections import OrderedDict


class MagicFunction:
	menu_storage = dict()
	custom_menu = OrderedDict([])

	def set_custom_menu(self, menu):
		self.custom_menu = menu

	def gen_keyboard(self, update):
		return ReplyKeyboardMarkup(self.get_markup(update), resize_keyboard=True)

	def get_markup(self, update):
		self.__create_storage(update)
		menu = self.menu_storage[update.message.chat_id]
		keyboard = menu.get_keyboard()
		return keyboard

	def text_menu(self, bot, update):
		self.__create_storage(update)
		menu = self.menu_storage[update.message.chat_id]
		menu.set_state(update.message.text)
		action = menu.get_action(self)
		return action(bot, update)

	def __create_storage(self, update):
		if update.message.chat_id not in self.menu_storage:
			self.menu_storage[update.message.chat_id] = MagicMenu(self.custom_menu, update.message.chat_id)
