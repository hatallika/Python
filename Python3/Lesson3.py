# Настройка webbhook для чат-бота
import logging
import os
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
from aiogram.utils.executor import start_webhook
from dotenv import load_dotenv

load_dotenv()

user_data = {}
# Настройки бота
API_TOKEN = os.getenv('TOKEN')
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

# Настройки webhooks
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{API_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# Настройки сервера
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)


def get_keyboard():
    buttons = [
        types.InlineKeyboardButton(text='-1', callback_data='num_decr'),
        types.InlineKeyboardButton(text='+1', callback_data='num_incr'),
        types.InlineKeyboardButton(text='Подтвердить', callback_data='num_finish'),
    ]

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard


async def update_text(message: types.Message, new_value: int):
    await message.edit_text(f'Укажите число: {new_value}', reply_markup=get_keyboard())


@dp.message_handler(commands='start')
async def cmd_number(message: types.Message):
    user_data[message.from_user.id] = 0
    await message.answer('Укажите число: 0', reply_markup=get_keyboard())


@dp.callback_query_handler(Text(startswith='num_'))
async def callback_nums(call: types.CallbackQuery):
    user_value = user_data.get(call.from_user.id, 0)
    action = call.data.split('_')[1]
    if action == 'decr':
        user_data[call.from_user.id] = user_value - 1
        await update_text(call.message, user_value - 1)
    elif action == 'incr':
        user_data[call.from_user.id] = user_value + 1
        await update_text(call.message, user_value + 1)
    elif action == 'finish':
        await call.message.edit_text(f'Итого {user_value}')
    await call.answer()


async def on_startup(dp: Dispatcher):
    await bot.set_webhook((WEBHOOK_URL))


async def on_shutdown(dp: Dispatcher):
    logging.warning('Отключаем')
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning('До свидания')


if __name__ == '__main__':
    # для теста программы запустим через пуллинг
    # executor.start_polling(dp, skip_updates=True)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT
    )
