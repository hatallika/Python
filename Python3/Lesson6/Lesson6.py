import os
from dotenv import load_dotenv
import logging
import datetime
from typing import Dict
from aiogram import Bot, Dispatcher, executor, types

load_dotenv()
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('aiogram').setLevel(logging.INFO)

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['time'])
async def start_time(message: types.Message):
    pass


@dp.callback_query_handler()
async def cb_handler(query: types.CallbackQuery, callback_data: Dict[str, str]):
    pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
