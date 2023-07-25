# Регистрация телеграмм бота ч2
import os
# from urllib.request import urlopen
# import json
#
# TOKEN = os.environ['TOKEN']
# r = urlopen(f'https://api.telegram.org/bot{TOKEN}/getUpdates').read()
# result = json.loads(r)
# print(result)
# chat_id = result['result'][0]['message']['chat']['id']
# user_name = result['result'][0]['message']['chat']['first_name']
# print(chat_id, user_name)
# text = f'Привет, {user_name}'
# r = urlopen(
#     f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text=Привет")
import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.environ['TOKEN']


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(text=['hello', 'hi'])
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.reply('Hi!')
    # await message.answer('Привет, я бот!')


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)
    # await message.answer('Привет, я бот!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
