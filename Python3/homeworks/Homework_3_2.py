# Формулировка задания:#
# Изучение API предоставляемое телеграмм
#
# Планируемый результат:#
# Изучение и практика в работе с API
import os
from urllib.request import urlopen
import json

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import logging

load_dotenv()

API_TOKEN = os.getenv('TOKEN')
# Работа напрямую с API

# Запрос
response = urlopen(f'https://api.telegram.org/bot{API_TOKEN}/getMe').read()
response = json.loads(response)
print(response)

response = urlopen(f'https://api.telegram.org/bot{API_TOKEN}/getUpdates').read()
result = json.loads(response)
print(result)
for item in result['result']:
    print(item)

chat_id = result['result'][0]['message']['chat']['id']
user_name = result['result'][0]['message']['chat']['first_name']
print(chat_id, user_name)
text = f'Привет, {user_name}'
r = urlopen(
    f"https://api.telegram.org/bot{API_TOKEN}/sendMessage?chat_id={chat_id}&text=Hello!")


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Configure logging
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='start')
async def start_button(message: types.Message):
    username = message.from_user.username
    first_name = message.from_user.first_name
    if first_name:
        name = first_name
    else:
        name = username

    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True)
    button1 = KeyboardButton('Вариант 1')
    button2 = KeyboardButton('Вариант 2')
    keyboard.add(button1)
    keyboard.add(button2)
    await message.answer(f'Привет, {name}\nВыберите вариант ответа...', reply_markup=keyboard)


@dp.message_handler(text=['Вариант 1', 'Вариант 2'])
async def replay_func(message: types.Message):
    await message.answer(f"Hello, выбран {message.text}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
