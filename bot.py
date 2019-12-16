import datetime
from logging import getLogger
from subprocess import Popen
from subprocess import PIPE

from telegram import Bot
from telegram import Update
from telegram import ParseMode
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CallbackQueryHandler
from telegram.utils.request import Request

TG_TOKEN = '1060473158:AAFHMygt8fWELbWpbaiQQ00JaKXHmy_JOiw'

logger = getLogger(__name__)

# `callback_data` -- это то, что будет присылать TG при нажатии на каждую кнопку.
# Поэтому каждый идентификатор должен быть уникальным
CALLBACK_BUTTON1_QAZAQ = "callback_button1_qazaq"
CALLBACK_BUTTON2_KYRGYZ = "callback_button2_kyrgyz"
CALLBACK_BUTTON3_RUSSIAN = "callback_button3_russian"
CALLBACK_BUTTON4_TADJIK = "callback_button4_tadjik"
CALLBACK_BUTTON5_QAZAQSTAN = "callback_button5_qazaqstan"
CALLBACK_BUTTON6_KYRGYZSTAN = "callback_button6_kyrgyzstan"
CALLBACK_BUTTON7_TADJIKISTAN = "callback_button7_tadjikistan"
CALLBACK_BUTTON8_CHAT1 = "callback_button8_chat"
CALLBACK_BUTTON9_CHAT2 = "callback_button9_chat"
CALLBACK_BUTTON10_CHAT3 = "callback_button10_chat"
CALLBACK_BUTTON11_CHAT4 = "callback_button11_chat"
CALLBACK_BUTTON12_CHAT5 = "callback_button12_chat"
CALLBACK_BUTTON13_CHAT6 = "callback_button13_chat"
CALLBACK_BUTTON14_FAQ1 = "callback_button14_faqqazrus"
CALLBACK_BUTTON15_FAQ2 = "callback_button15_faqqazqaz"
CALLBACK_BUTTON16_FAQ3 = "callback_button16_faqkyrgrus"
CALLBACK_BUTTON17_FAQ4 = "callback_button17_faqkyrgkyrg"
CALLBACK_BUTTON18_FAQ5 = "callback_button18_faqtadrus"
CALLBACK_BUTTON19_FAQ6 = "callback_button19_faqtadtad"
CALLBACK_BUTTON20_BACK1 = "callback_button20_back1"
CALLBACK_BUTTON21_BACK2 = "callback_button21_back2"
CALLBACK_BUTTON22_FORWARD1 = "callback_button22_forward1"
CALLBACK_BUTTON23_FORWARD2 = "callback_button23_forward2"
CALLBACK_BUTTON24_QUESTION = "callback_button24_question"
CALLBACK_BUTTON25_QAZAQ2 = "callback_button25_qazaq2"
CALLBACK_BUTTON26_KYRGYZ2 = "callback_button26_kyrgyz2"
CALLBACK_BUTTON27_RUSSIAN2 = "callback_button27_russian2"
CALLBACK_BUTTON28_TADJIK2 = "callback_button28_tadjik2"
CALLBACK_BUTTON29_QAZAQSTAN2 = "callback_button29_qazaqstan2"
CALLBACK_BUTTON30_KYRGYZSTAN2 = "callback_button30_kyrgyzstan2"
CALLBACK_BUTTON31_TADJIKISTAN2 = "callback_button31_tadjikistan2"

TITLES = {
	CALLBACK_BUTTON1_QAZAQ: "Казахский язык",
	CALLBACK_BUTTON2_KYRGYZ: "Кыргызский язык",
	CALLBACK_BUTTON3_RUSSIAN: "Русский язык",
	CALLBACK_BUTTON4_TADJIK: "Таджикский язык",
	CALLBACK_BUTTON5_QAZAQSTAN: "Казахстан🇰🇿",
	CALLBACK_BUTTON6_KYRGYZSTAN: "Кыргызстан🇰🇬",
	CALLBACK_BUTTON7_TADJIKISTAN: "Таджикистан🇹🇯",
	CALLBACK_BUTTON8_CHAT1: "Ссылка на чат",
	CALLBACK_BUTTON9_CHAT2: "Ссылка на чат",
	CALLBACK_BUTTON10_CHAT3: "Ссылка на чат",
	CALLBACK_BUTTON11_CHAT4: "Ссылка на чат",
	CALLBACK_BUTTON12_CHAT5: "Ссылка на чат",
	CALLBACK_BUTTON13_CHAT6: "Ссылка на чат",
	CALLBACK_BUTTON14_FAQ1: "FAQ",
	CALLBACK_BUTTON15_FAQ2: "FAQ",
	CALLBACK_BUTTON16_FAQ3: "FAQ",
	CALLBACK_BUTTON17_FAQ4: "FAQ",
	CALLBACK_BUTTON18_FAQ5: "FAQ",
	CALLBACK_BUTTON19_FAQ6: "FAQ",
	CALLBACK_BUTTON20_BACK1: "1",
	CALLBACK_BUTTON21_BACK2: "1",
	CALLBACK_BUTTON22_FORWARD1: "2",
	CALLBACK_BUTTON23_FORWARD2: "2",
	CALLBACK_BUTTON24_QUESTION :"Задать вопрос\n"
								"(эта функция еще не работает)",
	CALLBACK_BUTTON25_QAZAQ2: "Казахский язык",
	CALLBACK_BUTTON26_KYRGYZ2: "Кыргызский язык",
	CALLBACK_BUTTON27_RUSSIAN2: "Русский язык",
	CALLBACK_BUTTON28_TADJIK2: "Таджикский язык",
	CALLBACK_BUTTON29_QAZAQSTAN2: "Казахстан🇰🇿",
	CALLBACK_BUTTON30_KYRGYZSTAN2: "Кыргызстан🇰🇬",
	CALLBACK_BUTTON31_TADJIKISTAN2: "Таджикистан🇹🇯",
}

def get_base_inline_keyboard():
	#клавиатура с выбором язка
	keyboard = [

		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON1_QAZAQ], callback_data=CALLBACK_BUTTON1_QAZAQ),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON2_KYRGYZ], callback_data=CALLBACK_BUTTON2_KYRGYZ),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON3_RUSSIAN], callback_data=CALLBACK_BUTTON3_RUSSIAN),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON4_TADJIK], callback_data=CALLBACK_BUTTON4_TADJIK),
		],
	]
	return InlineKeyboardMarkup(keyboard)


def get_base_inline_keyboard1():
	# клавиатура с выбором язка для команды /chat
	keyboard = [

		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON25_QAZAQ2], callback_data=CALLBACK_BUTTON25_QAZAQ2),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON26_KYRGYZ2], callback_data=CALLBACK_BUTTON26_KYRGYZ2),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON27_RUSSIAN2], callback_data=CALLBACK_BUTTON27_RUSSIAN2),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON28_TADJIK2], callback_data=CALLBACK_BUTTON28_TADJIK2),
		],
	]
	return InlineKeyboardMarkup(keyboard)

def get_keyboard2():
	#клавиатура выбора страны (если выбрали русский язык)
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON5_QAZAQSTAN], callback_data=CALLBACK_BUTTON5_QAZAQSTAN),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON6_KYRGYZSTAN], callback_data=CALLBACK_BUTTON6_KYRGYZSTAN),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON7_TADJIKISTAN], callback_data=CALLBACK_BUTTON7_TADJIKISTAN),
		],
	]
	return InlineKeyboardMarkup(keyboard)

def get_keyboard2_2():
	#клавиатура выбора страны (если выбрали русский язык) для команды |chat
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON29_QAZAQSTAN2], callback_data=CALLBACK_BUTTON29_QAZAQSTAN2),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON30_KYRGYZSTAN2], callback_data=CALLBACK_BUTTON30_KYRGYZSTAN2),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON31_TADJIKISTAN2], callback_data=CALLBACK_BUTTON31_TADJIKISTAN2),
		],
	]
	return InlineKeyboardMarkup(keyboard)

def get_keyboard3_1():
	#приветственное сообщение для казахоговорящих казахов
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON9_CHAT2], callback_data=CALLBACK_BUTTON9_CHAT2),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON15_FAQ2], callback_data=CALLBACK_BUTTON15_FAQ2),
		],
	]
	return InlineKeyboardMarkup(keyboard)

def get_keyboard3_2():
	#приветственное сообщение для рускоговорящих казахов
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON8_CHAT1], callback_data=CALLBACK_BUTTON8_CHAT1),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON14_FAQ1], callback_data=CALLBACK_BUTTON14_FAQ1),
		],
	]
	return InlineKeyboardMarkup(keyboard)

def get_keyboard3_3():
	#приветственное сообщение для кыргызоговорящих кыргызов
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON11_CHAT4], callback_data=CALLBACK_BUTTON11_CHAT4),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON17_FAQ4], callback_data=CALLBACK_BUTTON17_FAQ4),
		],
	]
	return InlineKeyboardMarkup(keyboard)

def get_keyboard3_4():
	#приветственное сообщение для рускоговорящих кыргызов
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON10_CHAT3], callback_data=CALLBACK_BUTTON10_CHAT3),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON16_FAQ3], callback_data=CALLBACK_BUTTON16_FAQ3),
		],
	]
	return InlineKeyboardMarkup(keyboard)

def get_keyboard3_5():
	#приветственное сообщение для таджикоговорящих таджиков
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON12_CHAT5], callback_data=CALLBACK_BUTTON12_CHAT5),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON19_FAQ6], callback_data=CALLBACK_BUTTON19_FAQ6),
		],
	]
	return InlineKeyboardMarkup(keyboard)

def get_keyboard3_6():
	#приветственное сообщение для рускоговорящих таджиков
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON13_CHAT6], callback_data=CALLBACK_BUTTON13_CHAT6),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON18_FAQ5], callback_data=CALLBACK_BUTTON18_FAQ5),
		],
	]
	return InlineKeyboardMarkup(keyboard)

def get_keyboard4_1():
	#клавиатура получения ссылки на чат и вопросов для казахоговорящих казахов
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON20_BACK1], callback_data=CALLBACK_BUTTON20_BACK1),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON22_FORWARD1], callback_data=CALLBACK_BUTTON22_FORWARD1),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON24_QUESTION], callback_data=CALLBACK_BUTTON24_QUESTION),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON9_CHAT2], callback_data=CALLBACK_BUTTON9_CHAT2),
		],
	]
	return InlineKeyboardMarkup(keyboard)

def get_keyboard4_2():
	#клавиатура получения ссылки на чат и вопросов для русскоговорящих казахов
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON20_BACK1], callback_data=CALLBACK_BUTTON20_BACK1),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON22_FORWARD1], callback_data=CALLBACK_BUTTON22_FORWARD1),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON24_QUESTION], callback_data=CALLBACK_BUTTON24_QUESTION),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON8_CHAT1], callback_data=CALLBACK_BUTTON8_CHAT1),
		],
	]
	return InlineKeyboardMarkup(keyboard)

def get_keyboard4_3():
	#клавиатура получения ссылки на чат и вопросов для кыргызоговорящих кыргызов
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON20_BACK1], callback_data=CALLBACK_BUTTON20_BACK1),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON22_FORWARD1], callback_data=CALLBACK_BUTTON22_FORWARD1),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON24_QUESTION], callback_data=CALLBACK_BUTTON24_QUESTION),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON11_CHAT4], callback_data=CALLBACK_BUTTON11_CHAT4),
		],
	]
	return InlineKeyboardMarkup(keyboard)

def get_keyboard4_4():
	#клавиатура получения ссылки на чат и вопросов для русскоговорящих кыргызов
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON20_BACK1], callback_data=CALLBACK_BUTTON20_BACK1),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON22_FORWARD1], callback_data=CALLBACK_BUTTON22_FORWARD1),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON24_QUESTION], callback_data=CALLBACK_BUTTON24_QUESTION),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON10_CHAT3], callback_data=CALLBACK_BUTTON10_CHAT3),
		],
	]
	return InlineKeyboardMarkup(keyboard)

def get_keyboard4_5():
	#клавиатура получения ссылки на чат и вопросов для таджикоговорящих таджиков
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON20_BACK1], callback_data=CALLBACK_BUTTON20_BACK1),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON22_FORWARD1], callback_data=CALLBACK_BUTTON22_FORWARD1),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON24_QUESTION], callback_data=CALLBACK_BUTTON24_QUESTION),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON13_CHAT6], callback_data=CALLBACK_BUTTON13_CHAT6),
		],
	]
	return InlineKeyboardMarkup(keyboard)

def get_keyboard4_6():
	#клавиатура получения ссылки на чат и вопросов для русскоговорящих таджиков
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON20_BACK1], callback_data=CALLBACK_BUTTON20_BACK1),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON22_FORWARD1], callback_data=CALLBACK_BUTTON22_FORWARD1),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON24_QUESTION], callback_data=CALLBACK_BUTTON24_QUESTION),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON12_CHAT5], callback_data=CALLBACK_BUTTON12_CHAT5),
		],
	]
	return InlineKeyboardMarkup(keyboard)

def get_keyboard4_7():
	#вопрос-ответ для команды /question
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON21_BACK2], callback_data=CALLBACK_BUTTON21_BACK2),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON23_FORWARD2], callback_data=CALLBACK_BUTTON23_FORWARD2),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON24_QUESTION], callback_data=CALLBACK_BUTTON24_QUESTION),
		],
	]
	return InlineKeyboardMarkup(keyboard)

def keyboard_callback_handler(update: Update, context: CallbackContext):
	#обрабатка и пропись основного кнопочного алгоритма
	query = update.callback_query
	data = query.data
	now = datetime.datetime.now()

	chat_id = update.effective_message.chat_id
	current_text = update.effective_message.text

	if data == CALLBACK_BUTTON1_QAZAQ:
		query.edit_message_text(
			text=current_text,
			parse_mode=ParseMode.MARKDOWN,
		)
		context.bot.send_message(
			chat_id=chat_id,
			text="Вы выбрали казахский язык.\n\n"
				 "Добро пожаловать на Онлайн-марафон от Медиашколы CABAR.asia.\n"
				 "Цель марафона – создавать крутой и качественный контент!\n"
				 "Мы хотим, чтобы все услышали твойголос и твою историю. А еще ты сможешь выиграть крутые призы и даже поездку в Англию.\n"
				 "В этом МарафонБоте ты сможешь:\n"
				 "- получить ответы на вопросы, связанные с онлайн-марафоном;\n"
				 "- получить доступ к чату и куратору, который будет вести тебя до конца марафона.",
			reply_markup=get_keyboard3_1(),
		)
	if data == CALLBACK_BUTTON2_KYRGYZ:
		query.edit_message_text(
			text=current_text,
			parse_mode=ParseMode.MARKDOWN,
		)
		context.bot.send_message(
			chat_id=chat_id,
			text="Вы выбрали кыргызский язык.\n\n"
				 "Добро пожаловать на Онлайн-марафон от Медиашколы CABAR.asia.\n"
				 "Цель марафона – создавать крутой и качественный контент!\n"
				 "Мы хотим, чтобы все услышали твойголос и твою историю. А еще ты сможешь выиграть крутые призы и даже поездку в Англию.\n"
				 "В этом МарафонБоте ты сможешь:\n"
				 "- получить ответы на вопросы, связанные с онлайн-марафоном;\n"
				 "- получить доступ к чату и куратору, который будет вести тебя до конца марафона.",
			reply_markup=get_keyboard3_3(),
		)
	if data == CALLBACK_BUTTON4_TADJIK:
		query.edit_message_text(
			text=current_text,
			parse_mode=ParseMode.MARKDOWN,
		)
		context.bot.send_message(
			chat_id=chat_id,
			text="Вы выбрали таджикский язык.\n\n"
				 "Добро пожаловать на Онлайн-марафон от Медиашколы CABAR.asia.\n"
				 "Цель марафона – создавать крутой и качественный контент!\n"
				 "Мы хотим, чтобы все услышали твойголос и твою историю. А еще ты сможешь выиграть крутые призы и даже поездку в Англию.\n"
				 "В этом МарафонБоте ты сможешь:\n"
				 "- получить ответы на вопросы, связанные с онлайн-марафоном;\n"
				 "- получить доступ к чату и куратору, который будет вести тебя до конца марафона.",
			reply_markup=get_keyboard3_5(),
		)
	if data == CALLBACK_BUTTON3_RUSSIAN:
		query.edit_message_text(
			text=current_text,
			parse_mode=ParseMode.MARKDOWN,
		)
		context.bot.send_message(
			chat_id=chat_id,
			text="Вы выбрали русский язык!\n\n"
				 "Выберите страну проживания:",
			reply_markup=get_keyboard2(),
		)
	elif data == CALLBACK_BUTTON5_QAZAQSTAN:
		query.edit_message_text(
			text=current_text,
			parse_mode=ParseMode.MARKDOWN,
		)
		context.bot.send_message(
			chat_id=chat_id,
			text="Вы выбрали страну - Казахстан.\n\n"
				 "Добро пожаловать на Онлайн-марафон от Медиашколы CABAR.asia.\n"
				 "Цель марафона – создавать крутой и качественный контент!\n"
				 "Мы хотим, чтобы все услышали твойголос и твою историю. А еще ты сможешь выиграть крутые призы и даже поездку в Англию.\n"
				 "В этом МарафонБоте ты сможешь:\n"
				 "- получить ответы на вопросы, связанные с онлайн-марафоном;\n"
				 "- получить доступ к чату и куратору, который будет вести тебя до конца марафона.",
			reply_markup=get_keyboard3_2(),
		)
	elif data == CALLBACK_BUTTON6_KYRGYZSTAN:
		query.edit_message_text(
			text=current_text,
			parse_mode=ParseMode.MARKDOWN,
		)
		context.bot.send_message(
			chat_id=chat_id,
			text="Вы выбрали страну - Кыргызстан.\n\n"
				 "Добро пожаловать на Онлайн-марафон от Медиашколы CABAR.asia.\n"
				 "Цель марафона – создавать крутой и качественный контент!\n"
				 "Мы хотим, чтобы все услышали твойголос и твою историю. А еще ты сможешь выиграть крутые призы и даже поездку в Англию.\n"
				 "В этом МарафонБоте ты сможешь:\n"
				 "- получить ответы на вопросы, связанные с онлайн-марафоном;\n"
				 "- получить доступ к чату и куратору, который будет вести тебя до конца марафона.",
			reply_markup=get_keyboard3_4(),
		)
	elif data == CALLBACK_BUTTON7_TADJIKISTAN:
		query.edit_message_text(
			text=current_text,
			parse_mode=ParseMode.MARKDOWN,
		)
		context.bot.send_message(
			chat_id=chat_id,
			text="Вы выбрали страну - Таджикистан.\n\n"
				 "Добро пожаловать на Онлайн-марафон от Медиашколы CABAR.asia.\n"
				 "Цель марафона – создавать крутой и качественный контент!\n"
				 "Мы хотим, чтобы все услышали твойголос и твою историю. А еще ты сможешь выиграть крутые призы и даже поездку в Англию.\n"
				 "В этом МарафонБоте ты сможешь:\n"
				 "- получить ответы на вопросы, связанные с онлайн-марафоном;\n"
				 "- получить доступ к чату и куратору, который будет вести тебя до конца марафона.",
			reply_markup=get_keyboard3_6(),
		)
	elif data == CALLBACK_BUTTON8_CHAT1:
		query.edit_message_text(
			text=current_text,
		)
		context.bot.send_message(
			parse_mode=ParseMode.HTML,
			chat_id=chat_id,
			text='Вот ваша <a href="https://t.me/joinchat/F1JbshZUAKQwNAm7i51NPA">ссылка</a> на чат.',
			reply_markup=ReplyKeyboardRemove(),
		)
	elif data == CALLBACK_BUTTON9_CHAT2:
		query.edit_message_text(
			text=current_text,
		)
		context.bot.send_message(
			parse_mode=ParseMode.HTML,
			chat_id=chat_id,
			text='Вот ваша <a href="https://t.me/joinchat/F1JbshTm90dat3Uw8xoc7Q">ссылка</a> на чат.',
			reply_markup=ReplyKeyboardRemove(),
		)
	elif data == CALLBACK_BUTTON10_CHAT3:
		query.edit_message_text(
			text=current_text,
		)
		context.bot.send_message(
			parse_mode=ParseMode.HTML,
			chat_id=chat_id,
			text='Вот ваша <a href="https://t.me/joinchat/F1JbshRI5sHrslth0lWI5A">ссылка</a> на чат.',
			reply_markup=ReplyKeyboardRemove(),
		)
	elif data == CALLBACK_BUTTON11_CHAT4:
		query.edit_message_text(
			text=current_text,
		)
		context.bot.send_message(
			parse_mode=ParseMode.HTML,
			chat_id=chat_id,
			text='Вот ваша <a href="https://t.me/joinchat/F1JbshMyjE_uz6yJp8DZTg">ссылка</a> на чат.',
			reply_markup=ReplyKeyboardRemove(),
		)
	elif data == CALLBACK_BUTTON12_CHAT5:
		query.edit_message_text(
			text=current_text,
		)
		context.bot.send_message(
			parse_mode=ParseMode.HTML,
			chat_id=chat_id,
			text='Вот ваша <a href="https://t.me/joinchat/F1JbshZrhB99ZAd-mlG5iw">ссылка</a> на чат.',
			reply_markup=ReplyKeyboardRemove(),
		)
	elif data == CALLBACK_BUTTON13_CHAT6:
		query.edit_message_text(
			text=current_text,
		)
		context.bot.send_message(
			parse_mode=ParseMode.HTML,
			chat_id=chat_id,
			text='Вот ваша <a href="https://t.me/joinchat/F1JbshUgTCeb1sxFsl1i3Q">ссылка</a> на чат.',
			reply_markup=ReplyKeyboardRemove(),
		)
	elif data == CALLBACK_BUTTON14_FAQ1:
		query.edit_message_text(
			text=current_text,
			parse_mode=ParseMode.MARKDOWN,
		)
		context.bot.send_message(
			chat_id=chat_id,
			text="1: В каких социальных сетях проходит марафон?\n"
				 "В марафоне могут участвовать пользователи Facebook, Instagram, Twitter, VK.com, каналы Telegram, Viber.\n\n"
				 "2: Влияет ли количество подписчиков на мою победу?\n"
				 "На победу влияет только качество контента и ваш рост, как его создателя",
			reply_markup=get_keyboard4_2(),
		)
	elif data == CALLBACK_BUTTON15_FAQ2:
		query.edit_message_text(
			text=current_text,
			parse_mode=ParseMode.MARKDOWN,
		)
		context.bot.send_message(
			chat_id=chat_id,
			text="1: В каких социальных сетях проходит марафон?\n"
				 "В марафоне могут участвовать пользователи Facebook, Instagram, Twitter, VK.com, каналы Telegram, Viber.\n\n"
				 "2: Влияет ли количество подписчиков на мою победу?\n"
				 "На победу влияет только качество контента и ваш рост, как его создателя",
			reply_markup=get_keyboard4_1(),
		)
	elif data == CALLBACK_BUTTON16_FAQ3:
		query.edit_message_text(
			text=current_text,
			parse_mode=ParseMode.MARKDOWN,
		)
		context.bot.send_message(
			chat_id=chat_id,
			text="1: В каких социальных сетях проходит марафон?\n"
				 "В марафоне могут участвовать пользователи Facebook, Instagram, Twitter, VK.com, каналы Telegram, Viber.\n\n"
				 "2: Влияет ли количество подписчиков на мою победу?\n"
				 "На победу влияет только качество контента и ваш рост, как его создателя",
			reply_markup=get_keyboard4_4(),
		)
	elif data == CALLBACK_BUTTON17_FAQ4:
		# "Удалим" клавиатуру у прошлого сообщения
		# (на самом деле отредактируем его так, что текст останется тот же, а клаиватура пропадёт)
		query.edit_message_text(
			text=current_text,
			parse_mode=ParseMode.MARKDOWN,
		)
		# Отправим новое сообщение при нажатии на кнопку
		context.bot.send_message(
			chat_id=chat_id,
			text="1: В каких социальных сетях проходит марафон?\n"
				 "В марафоне могут участвовать пользователи Facebook, Instagram, Twitter, VK.com, каналы Telegram, Viber.\n\n"
				 "2: Влияет ли количество подписчиков на мою победу?\n"
				 "На победу влияет только качество контента и ваш рост, как его создателя",
			reply_markup=get_keyboard4_3(),
		)
	elif data == CALLBACK_BUTTON18_FAQ5:
		query.edit_message_text(
			text=current_text,
			parse_mode=ParseMode.MARKDOWN,
		)
		context.bot.send_message(
			chat_id=chat_id,
			text="1: В каких социальных сетях проходит марафон?\n"
				 "В марафоне могут участвовать пользователи Facebook, Instagram, Twitter, VK.com, каналы Telegram, Viber.\n\n"
				 "2: Влияет ли количество подписчиков на мою победу?\n"
				 "На победу влияет только качество контента и ваш рост, как его создателя",
			reply_markup=get_keyboard4_6(),
		)
	elif data == CALLBACK_BUTTON19_FAQ6:
		query.edit_message_text(
			text=current_text,
			parse_mode=ParseMode.MARKDOWN,
		)
		context.bot.send_message(
			chat_id=chat_id,
			text="1: В каких социальных сетях проходит марафон?\n"
				 "В марафоне могут участвовать пользователи Facebook, Instagram, Twitter, VK.com, каналы Telegram, Viber.\n\n"
				 "2: Влияет ли количество подписчиков на мою победу?\n"
				 "На победу влияет только качество контента и ваш рост, как его создателя",
			reply_markup=get_keyboard4_5(),
		)
	elif data == CALLBACK_BUTTON20_BACK1:
		query.edit_message_text(
			text="1: В каких социальных сетях проходит марафон?\n"
				 "В марафоне могут участвовать пользователи Facebook, Instagram, Twitter, VK.com, каналы Telegram, Viber.\n\n"
				 "2: Влияет ли количество подписчиков на мою победу?\n"
				 "На победу влияет только качество контента и ваш рост, как его создателя",
			reply_markup=get_keyboard4_1(),
		)
	elif data == CALLBACK_BUTTON22_FORWARD1:
		query.edit_message_text(
			text="3: Любой пользователь может участвовать в марафоне?\n"
				 "В марафоне может участвовать любой пользователь, однако в конкурсе на получение призов могут участвовать: пользователи Instagram или Twitter (минимум 100 подписчиков), каналы Telegram, Viber, YouTube (минимум 50 подписчиков), пользователи Facebook, VK.com (минимум 500 друзей).",
			reply_markup=get_keyboard4_1(),
		)
	elif data == CALLBACK_BUTTON20_BACK1:
		query.edit_message_text(
			text="1: В каких социальных сетях проходит марафон?\n"
				 "В марафоне могут участвовать пользователи Facebook, Instagram, Twitter, VK.com, каналы Telegram, Viber.\n\n"
				 "2: Влияет ли количество подписчиков на мою победу?\n"
				 "На победу влияет только качество контента и ваш рост, как его создателя",
			reply_markup=get_keyboard4_2(),
		)
	elif data == CALLBACK_BUTTON22_FORWARD1:
		query.edit_message_text(
			text="3: Любой пользователь может участвовать в марафоне?\n"
				 "В марафоне может участвовать любой пользователь, однако в конкурсе на получение призов могут участвовать: пользователи Instagram или Twitter (минимум 100 подписчиков), каналы Telegram, Viber, YouTube (минимум 50 подписчиков), пользователи Facebook, VK.com (минимум 500 друзей).",
			reply_markup=get_keyboard4_2(),
		)
	elif data == CALLBACK_BUTTON20_BACK1:
		query.edit_message_text(
			text="1: В каких социальных сетях проходит марафон?\n"
				 "В марафоне могут участвовать пользователи Facebook, Instagram, Twitter, VK.com, каналы Telegram, Viber.\n\n"
				 "2: Влияет ли количество подписчиков на мою победу?\n"
				 "На победу влияет только качество контента и ваш рост, как его создателя",
			reply_markup=get_keyboard4_3(),
		)
	elif data == CALLBACK_BUTTON22_FORWARD1:
		query.edit_message_text(
			text="3: Любой пользователь может участвовать в марафоне?\n"
				 "В марафоне может участвовать любой пользователь, однако в конкурсе на получение призов могут участвовать: пользователи Instagram или Twitter (минимум 100 подписчиков), каналы Telegram, Viber, YouTube (минимум 50 подписчиков), пользователи Facebook, VK.com (минимум 500 друзей).",
			reply_markup=get_keyboard4_3(),
		)
	elif data == CALLBACK_BUTTON20_BACK1:
		query.edit_message_text(
			text="1: В каких социальных сетях проходит марафон?\n"
				 "В марафоне могут участвовать пользователи Facebook, Instagram, Twitter, VK.com, каналы Telegram, Viber.\n\n"
				 "2: Влияет ли количество подписчиков на мою победу?\n"
				 "На победу влияет только качество контента и ваш рост, как его создателя",
			reply_markup=get_keyboard4_4(),
		)
	elif data == CALLBACK_BUTTON22_FORWARD1:
		query.edit_message_text(
			text="3: Любой пользователь может участвовать в марафоне?\n"
				 "В марафоне может участвовать любой пользователь, однако в конкурсе на получение призов могут участвовать: пользователи Instagram или Twitter (минимум 100 подписчиков), каналы Telegram, Viber, YouTube (минимум 50 подписчиков), пользователи Facebook, VK.com (минимум 500 друзей).",
			reply_markup=get_keyboard4_4(),
		)
	elif data == CALLBACK_BUTTON20_BACK1:
		query.edit_message_text(
			text="1: В каких социальных сетях проходит марафон?\n"
				 "В марафоне могут участвовать пользователи Facebook, Instagram, Twitter, VK.com, каналы Telegram, Viber.\n\n"
				 "2: Влияет ли количество подписчиков на мою победу?\n"
				 "На победу влияет только качество контента и ваш рост, как его создателя",
			reply_markup=get_keyboard4_5(),
		)
	elif data == CALLBACK_BUTTON22_FORWARD1:
		query.edit_message_text(
			text="3: Любой пользователь может участвовать в марафоне?\n"
				 "В марафоне может участвовать любой пользователь, однако в конкурсе на получение призов могут участвовать: пользователи Instagram или Twitter (минимум 100 подписчиков), каналы Telegram, Viber, YouTube (минимум 50 подписчиков), пользователи Facebook, VK.com (минимум 500 друзей).",
			reply_markup=get_keyboard4_5(),
		)
	elif data == CALLBACK_BUTTON20_BACK1:
		query.edit_message_text(
			text="1: В каких социальных сетях проходит марафон?\n"
				 "В марафоне могут участвовать пользователи Facebook, Instagram, Twitter, VK.com, каналы Telegram, Viber.\n\n"
				 "2: Влияет ли количество подписчиков на мою победу?\n"
				 "На победу влияет только качество контента и ваш рост, как его создателя",
			reply_markup=get_keyboard4_6(),
		)
	elif data == CALLBACK_BUTTON22_FORWARD1:
		query.edit_message_text(
			text="3: Любой пользователь может участвовать в марафоне?\n"
				 "В марафоне может участвовать любой пользователь, однако в конкурсе на получение призов могут участвовать: пользователи Instagram или Twitter (минимум 100 подписчиков), каналы Telegram, Viber, YouTube (минимум 50 подписчиков), пользователи Facebook, VK.com (минимум 500 друзей).",
			reply_markup=get_keyboard4_6(),
		)
	elif data == CALLBACK_BUTTON21_BACK2:
		query.edit_message_text(
			text="1: В каких социальных сетях проходит марафон?\n"
				 "В марафоне могут участвовать пользователи Facebook, Instagram, Twitter, VK.com, каналы Telegram, Viber.\n\n"
				 "2: Влияет ли количество подписчиков на мою победу?\n"
				 "На победу влияет только качество контента и ваш рост, как его создателя",
			reply_markup=get_keyboard4_7(),
		)
	elif data == CALLBACK_BUTTON23_FORWARD2:
		query.edit_message_text(
			text="3: Любой пользователь может участвовать в марафоне?\n"
				 "В марафоне может участвовать любой пользователь, однако в конкурсе на получение призов могут участвовать: пользователи Instagram или Twitter (минимум 100 подписчиков), каналы Telegram, Viber, YouTube (минимум 50 подписчиков), пользователи Facebook, VK.com (минимум 500 друзей).",
			reply_markup=get_keyboard4_7(),
		)
	elif data == CALLBACK_BUTTON24_QUESTION:
		query.edit_message_text(
			text=current_text,
			parse_mode=ParseMode.MARKDOWN,
		)
		context.bot.send_message(
			chat_id=chat_id,
			text="*ссылка на чат с человеком, отвечающим на вопросы*",
			reply_markup=ReplyKeyboardRemove(),
		)
	if data == CALLBACK_BUTTON25_QAZAQ2:
		query.edit_message_text(
			text=current_text,
		)
		context.bot.send_message(
			parse_mode=ParseMode.HTML,
			chat_id=chat_id,
			text='Вы выбрали казахский язык (и страну Казахстан соответсвтенно).\n'
				 'Вот ваша <a href="https://t.me/joinchat/F1JbshTm90dat3Uw8xoc7Q">ссылка</a>.',
			reply_markup=ReplyKeyboardRemove(),
		)
	if data == CALLBACK_BUTTON26_KYRGYZ2:
		query.edit_message_text(
			text=current_text,
		)
		context.bot.send_message(
			parse_mode=ParseMode.HTML,
			chat_id=chat_id,
			text='Вы выбрали кыргызский язык (и страну Кыргызстан соответственно).\n'
				 'Вот ваша <a href="https://t.me/joinchat/F1JbshMyjE_uz6yJp8DZTg">ссылка</a>.',
			reply_markup=ReplyKeyboardRemove(),
		)
	if data == CALLBACK_BUTTON28_TADJIK2:
		query.edit_message_text(
			text=current_text,
		)
		context.bot.send_message(
			parse_mode=ParseMode.HTML,
			chat_id=chat_id,
			text='Вы выбрали таджикский язык (и страну Таджикистан соответстенно).\n'
				 'Вот ваша <a href="https://t.me/joinchat/F1JbshUgTCeb1sxFsl1i3Q">ссылка</a>.',
			reply_markup=ReplyKeyboardRemove(),
		)
	if data == CALLBACK_BUTTON27_RUSSIAN2:
		query.edit_message_text(
			text=current_text,
			parse_mode=ParseMode.MARKDOWN,
		)
		context.bot.send_message(
			chat_id=chat_id,
			text="Вы выбрали русский язык!\n"
				 "Выберите пожалуйста страну проживания:",
			reply_markup=get_keyboard2_2(),
		)
	elif data == CALLBACK_BUTTON29_QAZAQSTAN2:
		query.edit_message_text(
			text=current_text,
		)
		context.bot.send_message(
			parse_mode=ParseMode.HTML,
			chat_id=chat_id,
			text='Вы выбрали страну - Казахстан.\n'
				 'Вот ваша <a href="https://t.me/joinchat/F1JbshZUAKQwNAm7i51NPA">ссылка</a>.',
			reply_markup=ReplyKeyboardRemove(),
		)
	elif data == CALLBACK_BUTTON30_KYRGYZSTAN2:
		query.edit_message_text(
			text=current_text,
		)
		context.bot.send_message(
			parse_mode=ParseMode.HTML,
			chat_id=chat_id,
			text='Вы выбрали страну - Кыргызстан.\n'
				 'Вот ваша <a href="https://t.me/joinchat/F1JbshRI5sHrslth0lWI5A">ссылка</a>.',
			reply_markup=ReplyKeyboardRemove(),
		)
	elif data == CALLBACK_BUTTON31_TADJIKISTAN2:
		query.edit_message_text(
			text=current_text,
		)
		context.bot.send_message(
			parse_mode=ParseMode.HTML,
			chat_id=chat_id,
			text='Вы выбрали страну - Таджикистан.\n'
				 'Вот ваша <a href="https://t.me/joinchat/F1JbshZrhB99ZAd-mlG5iw">ссылка</a>.',
			reply_markup=ReplyKeyboardRemove(),
		)

def do_question(update: Update, context: CallbackContext):
	update.message.reply_text(
	text="1: В каких социальных сетях проходит марафон?\n"
				 "В марафоне могут участвовать пользователи Facebook, Instagram, Twitter, VK.com, каналы Telegram, Viber.\n\n"
				 "2: Влияет ли количество подписчиков на мою победу?\n"
				 "На победу влияет только качество контента и ваш рост, как его создателя",
	reply_markup=get_keyboard4_7()
	)


def do_chat(update: Update, context: CallbackContext):
	update.message.reply_text(
		text='Вы воспользовались командой "/chat". Пожалуйста, ответьте снова на некоторые вопросы:\n\n'
			 'Выберите свой язык:',
		reply_markup=get_base_inline_keyboard1()
	)

def do_start(update: Update, context: CallbackContext):
	update.message.reply_text(
		text="Здравствуйте!\n"
			 "Пожалуйста, выберите свой язык:",
		reply_markup=get_base_inline_keyboard(),
    )

def main():
    request = Request(
        connect_timeout=0.5,
        read_timeout=1.0
    )
    bot = Bot(
        request=request,
        token=TG_TOKEN,
    )
    updater = Updater(
        bot=bot,
        use_context=True,
    )
    question_handler = CommandHandler("question", do_question)
    chat_handler = CommandHandler("chat", do_chat)
    start_handler = CommandHandler("start", do_start)
    buttons_handler = CallbackQueryHandler(callback=keyboard_callback_handler)

    updater.dispatcher.add_handler(question_handler)
    updater.dispatcher.add_handler(chat_handler)
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(buttons_handler)

    print(bot.get_me())

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
