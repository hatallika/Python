# Команды телеграмм бота
# Реализация использования основных команд в чат боте
# Реализация и обработка основных команд

# выполнен разбор основных команд бота и их обработка Command, StartCommand,
# Обработка команд через кнопки разного типа(inline, repeat),
# обработка inline button с использованием фабрики колбеков

import os
from random import randint
from dotenv import load_dotenv

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, CallbackQuery
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters import Command, CommandStart, Text
from aiogram import Bot, Dispatcher, types, executor

load_dotenv()

TOKEN = os.getenv('TOKEN')
URL_GOOGLE = 'https://www.google.com/'
URL_YANDEX = 'https://www.ya.ru/'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

url_callback = CallbackData('url', 'item_name')

choice = InlineKeyboardMarkup(row_width=2)
url_button1 = InlineKeyboardButton('Button1', callback_data=url_callback.new('button1'))
url_button2 = InlineKeyboardButton('Button2', callback_data=url_callback.new('button2'))
cancel = InlineKeyboardButton(text='Отмена', callback_data='cancel')

choice.insert(url_button1)
choice.insert(url_button2)
choice.insert(cancel)

button1_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Перейти в Google', url=URL_GOOGLE)
    ],
])
button2_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Перейти в Yandex', url=URL_YANDEX)
    ],
])


@dp.message_handler(CommandStart())
async def start_bot(message: types.Message):
    buttons = [
        [KeyboardButton(text='/random')],
        [KeyboardButton(text='/links')],
    ]
    menu = ReplyKeyboardMarkup(keyboard=buttons)

    await message.answer('Выберите действие', reply_markup=menu)


# Генерация случайного числа по нажатию кнопки
@dp.message_handler(Command('random'))
async def cmd_random(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text='Нажми меня', callback_data='random_value'))
    await message.answer('Нажмите на кнопку для генерации числа от 1 до 10', reply_markup=keyboard)


# Обработка inline_button с callback_data
@dp.callback_query_handler(text='random_value')
async def sent_random_value(call: types.CallbackQuery):
    await call.message.answer(str(randint(1, 10)))
    await call.answer(text='Спасибо, что воспользовались ботом', show_alert=True)
    # Дождаличь ответа (Убрали часики)
    # await call.answer()


@dp.message_handler(Command('links'))
async def show_item(message: types.Message):
    await message.answer(text='Здравствуйте, выберите необходимую ссылку', reply_markup=choice)


@dp.callback_query_handler(url_callback.filter(item_name=['button1']))
async def get_google_url(call: CallbackQuery):
    await call.answer(cache_time=10)
    await call.message.answer('Вы выбрали Button1', reply_markup=button1_keyboard)


@dp.callback_query_handler(text_contains='button2')
async def get_google_url(call: CallbackQuery):
    await call.answer(cache_time=10)
    await call.message.answer('Вы выбрали Button2', reply_markup=button2_keyboard)


@dp.callback_query_handler(text='cancel')
async def cancel_bot(call: CallbackQuery):
    await call.answer('Вы нажали отмену')
    # убрали клавиатуру
    await call.message.edit_reply_markup(reply_markup=None)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
