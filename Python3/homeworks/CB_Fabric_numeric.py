import os
from contextlib import suppress

from aiogram.utils.exceptions import MessageNotModified
from dotenv import load_dotenv
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram import Bot, Dispatcher, types, executor
import config

load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# Фабрика колбеков
# cb = CallbackData("post", "id", "action")
# button = InlineKeyboardButton(text='Лайкнуть', callback_data=cb.new(id=5, action='like'))

# Обработка фабрики колбеков
# @dp.callback_query_handler(cb.filter())
# async def callbacks(call: types.CallbackQuery, callback_data: dict):
#     post_id = callback_data[id]
#     action = callback_data['action']


user_data = {}
callback_numbers = CallbackData("fabnum", "action")



# Получим клавиатуру
def get_keyboard_fab():
    buttons = [
        InlineKeyboardButton(text='-1', callback_data=callback_numbers.new(action='decr')),
        InlineKeyboardButton(text='+1', callback_data=callback_numbers.new(action='incr')),
        InlineKeyboardButton(text='Подтвердить', callback_data=callback_numbers.new(action='finish')),
    ]
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


# Обновить текст
async def update_num_text_fab(message: types.Message, new_value: int):
    with suppress(MessageNotModified):
        await message.edit_text(f'Укажите число: {new_value}', reply_markup=get_keyboard_fab())


@dp.message_handler(commands='numbers')
async def cmd_numbers(message: types.Message):
    user_data[message.from_user.id] = 0
    await message.answer('Укажите число: 0', reply_markup=get_keyboard_fab())


@dp.callback_query_handler(callback_numbers.filter(action=['incr', 'decr']))
async def callbacks_num(call: types.CallbackQuery, callback_data: dict):
    # Получаем текущее значение для пользователя, либо считаем его равным 0
    user_value = user_data.get(call.from_user.id, 0)
    # Получаем часть data из callback_data
    action = callback_data['action']
    match action:
        case 'incr':
            user_data[call.from_user.id] = user_value + 1
            await update_num_text_fab(call.message, user_value + 1)
        case 'decr':
            user_data[call.from_user.id] = user_value - 1
            await update_num_text_fab(call.message, user_value - 1)
        case _:
            print('Ошибка')
    await call.answer()


@dp.callback_query_handler(callback_numbers.filter(action=['finish']))
async def callbacks_num_finish_fab(call: types.CallbackQuery):
    user_value = user_data.get(call.from_user.id, 0)
    await call.message.edit_text(f'Итого: {user_value}')
    await call.answer()
