# Введение в Telegram API. Семинар
import os
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.exceptions import BotBlocked

# from dotenv import load_dotenv
# load_dotenv()
# TOKEN = os.getenv('TOKEN')

# TOKEN = os.environ['TOKEN']

TOKEN = os.getenv('TOKEN')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


# async def hello(message: types.Message):
#     await message.answer('Hello!')
#
#
# dp.register_message_handler(hello, commands='hello')
#
#
# @dp.message_handler(commands=['start', 'go'])
# async def start_bot(m: types.Message):
#     username = m.from_user.username
#     await m.answer(f'<i>Привет</i>, <b>{username}</b>. Я бот <a href="https://www.ya.ru">Yandex</a>')
#
#
# @dp.message_handler(text='Reply')
# async def replay_func(message: types.Message):
#     await message.reply("Hello, it's Reply")
#
#
# @dp.message_handler(commands='dice')
# async def dice_func(message: types.Message):
#     await message.answer_dice('🎯')  # по умолчанию кубик


# @dp.errors_handler(exception=BotBlocked)
# async def exception_func(message: types.Update, exception: BotBlocked):
#     print('Бот заблокировал пользователя')
#     return True


@dp.message_handler(commands='start')
async def start_button(message: types.Message):
    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True)
    button1 = KeyboardButton('Да')
    button2 = KeyboardButton('Нет')
    keyboard.add(button1)
    keyboard.add(button2)

    await message.answer('Ответьте...', reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
