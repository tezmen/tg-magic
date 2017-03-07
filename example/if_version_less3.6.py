# -*- coding: utf-8 -*-
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater

from tgmagic.buttons import PrevButton
from tgmagic.bot import MagicFunction
from tgmagic.helper import menu

from collections import OrderedDict

"""
Because the sort was saved only in the python3.6 (PEP 468: Preserving Keyword Argument Order),
you can use the following structure to store the order of items in the menu
"""
my_custom_menu = OrderedDict([
	('menu', OrderedDict([
		('magic', '🔮Магия'),
		('magic_nested', OrderedDict([
			('fire', '🔥Огненный шар!'),
			('cold', '❄️Ледяной шип'),
			('prev', PrevButton('◀️Назад'))
		]))
	]))
])


class TestBot(MagicFunction):
	def start(self, bot, update):
		bot.sendMessage(
			text='Привет, странник!',
			chat_id=update.message.chat_id,
			reply_markup=self.gen_keyboard(update)
		)

	def magic(self, bot, update):
		bot.sendMessage(
			text='Заклинания? Чтож, какое ты хочешь использовать?',
			chat_id=update.message.chat_id,
			reply_markup=self.gen_keyboard(update)
		)

	def fire(self, bot, update):
		bot.sendMessage(
			text='Бог карает огнём. Я тоже!',
			chat_id=update.message.chat_id,
			reply_markup=self.gen_keyboard(update)
		)

	def cold(self, bot, update):
		bot.sendMessage(
			text='Время сосулек, сучки!',
			chat_id=update.message.chat_id,
			reply_markup=self.gen_keyboard(update)
		)

	def prev(self, bot, update):
		bot.sendMessage(
			text='Возращаемся назад...',
			chat_id=update.message.chat_id,
			reply_markup=self.gen_keyboard(update)
		)

	@menu
	def text(self, bot, update):
		# ...
		# and any other handlers
		pass

	def main(self):
		self.set_custom_menu(my_custom_menu)
		updater = Updater('API:KEY')
		dp = updater.dispatcher
		dp.add_handler(CommandHandler('start', self.start))
		dp.add_handler(MessageHandler(Filters.text, self.text))
		updater.start_polling()


TestBot().main()
