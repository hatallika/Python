# Lesson Систкма платежей
# Inline Режим (14:50) @youtube 'Название фильмаэ'

# Например мы создали БД
# CREATE TABLE IF NOT EXIST 'films' (
#     'user_id' INTEGER NOT NULL,
#     'films_hash TEXT NOT NULL',
#     'descriprion TEXT NOT NULL'
# )
# from aiogram import types
#
#
# # Нам нужна обработка данных
# async def inline_handler(query: types.InlineQuery):
#     user_links =


# скопируем пример бота с прошлых уроков ( Database)

import os
import logging
import sqlite3
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import CommandStart

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Логирование
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='inline')
async def cmd_inline(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text='Текст1', callback_data='text1'),
        types.InlineKeyboardButton(text='Текст2', callback_data='text2'),
    ]

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer('111', reply_markup=keyboard)


@dp.callback_query_handler(text='text1')
async def text1(call: types.CallbackQuery):
    # Ответ всплывающим окном
    await call.answer('Спасибо за то, что воспользовались нашим ботом')

@dp.callback_query_handler(text='text2')
async def text2(call: types.CallbackQuery):
    await call.answer('Спасибо за то, что воспользовались нашим ботом')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
