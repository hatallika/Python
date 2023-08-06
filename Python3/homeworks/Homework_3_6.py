# Домашнее задание 3.6
# Формулировка задания: Реализация Inline клавиатуры в чат боте
# Планируемый результат: Inline клавиатура в телеграмм боте

import os

from aiogram.dispatcher.filters import CommandStart
from aiogram.utils.callback_data import CallbackData
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging

load_dotenv()
TOKEN = os.getenv('TOKEN')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Фабрика колбеков
cb = CallbackData("input", "value", "action")
cb_operation = CallbackData("operation", "action")
# button = InlineKeyboardButton(text='Лайкнуть', callback_data=cb.new(id=5, action='like'))

# Обработка фабрики колбеков
# @dp.callback_query_handler(cb.filter())
# async def callbacks(call: types.CallbackQuery, callback_data: dict):
#     post_id = callback_data[id]
#     action = callback_data['action']

num_list = []
values_list = []
operator = []
nums_keyboard = InlineKeyboardMarkup(row_width=3)
for i in range(9, -1, -1):
    nums_keyboard.insert(InlineKeyboardButton(str(i), callback_data=cb.new(value=str(i), action='add_num')))

nums_keyboard.row(
    InlineKeyboardButton('+', callback_data=cb_operation.new(action='+')),
    InlineKeyboardButton('-', callback_data=cb_operation.new(action='-')),
    InlineKeyboardButton('%', callback_data=cb_operation.new(action='/')),
    InlineKeyboardButton('*', callback_data=cb_operation.new(action='*'))
)
nums_keyboard.add(InlineKeyboardButton('=', callback_data='equal'))


def insert_value():
    if len(num_list) == 0:
        num_list.append('0')
        print(num_list)
    # запомним вводимое пользователем значение как число для операции с ним
    values_list.append(''.join(num_list))
    print(values_list)
    # очистим набор числа для нового набора после операции
    num_list.clear()


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer('Калькулятор', reply_markup=nums_keyboard)


@dp.callback_query_handler(cb.filter())
async def set_to_num_list(call: types.CallbackQuery, callback_data: dict):
    num = callback_data['value']
    num_list.append(num)
    print(num_list)
    await call.message.edit_text(
        ''.join(num_list) if len(operator) < 1 else f'{values_list[0]} {operator[0]} {"".join(num_list)}',
        reply_markup=nums_keyboard)


@dp.callback_query_handler(cb_operation.filter())
async def add_operation(call: types.CallbackQuery, callback_data: dict):
    # запомним оператор
    operator.append(callback_data['action'])
    print(operator)
    insert_value()
    await call.message.edit_text(f'{values_list[0]} {operator[0]}', reply_markup=nums_keyboard)


@dp.callback_query_handler(text='equal')
async def equal_func(call: types.CallbackQuery):
    result = 0
    str_ = ''
    insert_value()
    print('=', values_list)
    if len(operator) == 0:
        values_list.clear()
        result = 0

    if len(operator) > 0:
        if operator[0] == '+':
            result = int(values_list[0]) + int(values_list[1])
            print(result)
        elif operator[0] == '-':
            result = int(values_list[0]) - int(values_list[1])
        elif operator[0] == '/':
            if values_list[1] != '0':
                result = int(values_list[0]) / int(values_list[1])
            else:
                return await call.answer('На 0 делить нельзя')
        elif operator[0] == '*':
            result = int(values_list[0]) * int(values_list[1])

        str_ = f'{values_list[0]} {operator[0]} {values_list[1]}'
        operator.clear()
        values_list.clear()
    await call.message.edit_text(f'Результат: {str_}  = {result}', reply_markup=nums_keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
