# Обработка сообщений в чат боте. Семинар

import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import CommandStart, Command, ChatTypeFilter
from aiogram.types import Update
import re

load_dotenv()
TOKEN = os.getenv('TOKEN')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# @dp.message_handler(text='Привет')
# async def start_bot(message: types.Message):
#     await message.answer(f'Привет, {message.from_user.username}')


# @dp.message_handler(CommandStart(deep_link='Привет'))
# async def start_bot(message: types.Message):
#     await message.answer(text='Ты нажал на старт и передал аргумент Привет')

#
# @dp.message_handler(CommandStart())
# async def start_bot(message: types.Message):
#     # Для передачи аргументов в /start, пользователь должен ввести https://t.me/HatallikaBot?start=Hello
#     args = message.get_args()
#     await message.answer(f'Привет, я бот! Вы передали аргументы {args}')

# Регулярное выражение в deep_link команды
# @dp.message_handler(CommandStart(deep_link=re.compile(r'^[0-9]{4,15}$')))
# async def start_bot(message: types.Message):
#     referral = message.get_args()
#     await message.answer(f'Вас привел пользователь {referral}')


# @dp.message_handler(CommandStart(deep_link=re.compile(r'\d\d\d$')))
# async def start_bot(message: types.Message):
#     await message.answer(f'Вы передали правильный диплинк {message.get_args()}')

# @dp.message_handler(CommandStart())
# async def start_bot(message: types.Message):
#     await message.answer('Hello')
#
#
# @dp.message_handler(ChatTypeFilter(types.ChatType.PRIVATE), user_id=[426556664], text='hello')
# async def start_bot(message: types.Message):
#     await message.answer('Hello world')


@dp.message_handler(CommandStart())
async def start_bot(message: types.Message):
    try:
        await message.answer(1 / 0)
    except Exception as err:
        await message.answer(f'Не попало в error handler\n {err}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


@dp.errors_handler()
async def start_bot(update: types.Update, exception):
    # await Update.message
    await update.get_current().message.answer(f'Ошибка {exception}')
