# -*- coding: utf-8 -*-
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
import os

from tgmagic.buttons import PrevButton
from tgmagic.bot import MagicFunction
from tgmagic.helper import menu

my_custom_menu = {
	'menu': {
		'magic': '🔮Магия',
		'magic_nested': {
			'fire': '🔥Огненный шар!',
			'cold': '❄️Ледяной шип',
			'prev': PrevButton('◀️Назад')
		},
		'inventory': '⛏Инвентарь',
		'inventory_nested': {
			'potion': '⚗Зелья',
			'armor': '🛡Броня',
			'weapon': '⚔Оружие',
			'prev': PrevButton('◀️Назад'),
			'weapon_nested': {
				'sword': '🗡Меч',
				'knife': '🔪Нож',
				'prev': PrevButton('◀️Назад')
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

	def inventory(self, bot, update):
		bot.sendMessage(
			text='Что ты хочешь посмотреть в инвентаре?',
			chat_id=update.message.chat_id,
			reply_markup=self.gen_keyboard(update)
		)

	def potion(self, bot, update):
		text = 'К сожалению, у тебя нет зелий :(' + os.linesep
		text += 'Возвращайся, когда обучишься алхимии!' + os.linesep
		bot.sendMessage(
			text=text,
			chat_id=update.message.chat_id,
			reply_markup=self.gen_keyboard(update)
		)

	def armor(self, bot, update):
		text = 'К сожалению, у тебя нет брони :(' + os.linesep
		text += 'Беззащитный воин? И как жить-то будешь?' + os.linesep
		bot.sendMessage(
			text=text,
			chat_id=update.message.chat_id,
			reply_markup=self.gen_keyboard(update)
		)

	def weapon(self, bot, update):
		bot.sendMessage(
			text='Каким оружием ты хочешь воспользоваться?',
			chat_id=update.message.chat_id,
			reply_markup=self.gen_keyboard(update)
		)

	def magic(self, bot, update):
		bot.sendMessage(
			text='Заклинания? Чтож, какое ты хочешь использовать?',
			chat_id=update.message.chat_id,
			reply_markup=self.gen_keyboard(update)
		)

	def sword(self, bot, update):
		bot.sendMessage(
			text='🗡Один прогиб и ты погиб. Один удар и ты разрублен на куски! 🗡',
			chat_id=update.message.chat_id,
			reply_markup=self.gen_keyboard(update)
		)

	def knife(self, bot, update):
		bot.sendMessage(
			text='🔪Нож в печень – никто не вечен!',
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
