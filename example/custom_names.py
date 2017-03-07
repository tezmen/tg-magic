# -*- coding: utf-8 -*-
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater

from tgmagic.buttons import PrevButton
from tgmagic.bot import MagicFunction
from tgmagic.helper import menu

"""
Editing predefined keys for menu dict
If you edit previous key, you also need to rename your function, which is responsible for the step back.
"""
from tgmagic.buttons import ExtendNames
ExtendNames().start_element = 'menu1'
ExtendNames().previous = 'back'
ExtendNames().nested = 'xxx'

my_custom_menu = {
	'menu1': {
		'magic': '🔮Магия',
		'magic_xxx': {
			'fire': '🔥Огненный шар!',
			'cold': '❄️Ледяной шип',
			'back': PrevButton('◀️Назад')
		},
		'inventory': '⛏Инвентарь',
		'inventory_xxx': {
			'potion': '⚗Зелья',
			'armor': '🛡Броня',
			'weapon': '⚔Оружие',
			'back': PrevButton('◀️Назад'),
			'weapon_xxx': {
				'sword': '🗡Меч',
				'knife': '🔪Нож',
				'back': PrevButton('◀️Назад')
			}
		},
	}
}


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

	def back(self, bot, update):
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
