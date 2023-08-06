# Клавиатуры в Telegram (2)
import os

from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardRemove

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# button_hi = KeyboardButton('Привет! 👋')
#
# greet_kb = ReplyKeyboardMarkup()
# greet_kb.add(button_hi)
#
# greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)
# greet_kb2 = ReplyKeyboardMarkup(
#     resize_keyboard=True, one_time_keyboard=True,
# ).add(button_hi)
#
#
# @dp.message_handler(commands='start')
# async def start_bot(message: types.Message):
#     await message.answer('Привет', reply_markup=greet_kb)
#
#
# @dp.message_handler(commands='hi1')
# async def func_hi1(message: types.Message):
#     await message.answer('Изменяем размер клавиатуры', reply_markup=greet_kb1)
#
#
# @dp.message_handler(commands='hi2')
# async def func_hi2(message: types.Message):
#     await message.answer('Прячем клавиатуру', reply_markup=greet_kb2)


# button1 = KeyboardButton('1️⃣')
# button2 = KeyboardButton('2️⃣')
# button3 = KeyboardButton('3️⃣')
#
# markup1 = ReplyKeyboardMarkup(one_time_keyboard=True).add(button1).add(button2).add(button3)
# markup2 = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).row(button1, button2, button3)
# markup3 = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).row(button1, button2, button3).add(
#     KeyboardButton('Средний ряд')
# )
#
# button4 = KeyboardButton('4️⃣')
# button5 = KeyboardButton('5️⃣')
# button6 = KeyboardButton('6️⃣')
#
# markup3.add(button4, button5)
# markup3.insert(button6)


# @dp.message_handler(commands='hi3')
# async def func_hi3(message: types.Message):
#     await message.answer('Добавим больше кнопок', reply_markup=markup1)
#
#
# @dp.message_handler(commands='hi4')
# async def func_hi4(message: types.Message):
#     await message.answer('Строка кнопок', reply_markup=markup2)
#
#
# @dp.message_handler(commands='hi5')
# async def func_hi5(message: types.Message):
#     await message.answer('Комбинация', reply_markup=markup3)

# markup_request = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
#     KeyboardButton('Отправить контакт 📞', request_contact=True)
# ).add(KeyboardButton('Отправить локацию 🗺', request_location=True))
#
#
# @dp.message_handler(commands='hi6')
# async def func_hi6(message: types.Message):
#     await message.answer('h16', reply_markup=markup_request)

# button1 = KeyboardButton('1️⃣')
# button2 = KeyboardButton('2️⃣')
# button3 = KeyboardButton('3️⃣')
#
# button4 = KeyboardButton('4️⃣')
# button5 = KeyboardButton('5️⃣')
# button6 = KeyboardButton('6️⃣')
#
# # markup_big = ReplyKeyboardMarkup(one_time_keyboard=True)
# markup_big = ReplyKeyboardMarkup()
#
# markup_big.add(button1, button2, button3, button4, button5, button6)
# markup_big.row(button1, button2, button3, button4, button5, button6)
# markup_big.row(button4, button2)
# markup_big.add(button3, button2)
# markup_big.insert(button1)
# markup_big.insert(button6)
# markup_big.insert(KeyboardButton('9️⃣'))


# @dp.message_handler(commands='hi7')
# async def func_hi6(message: types.Message):
#     await message.answer('big', reply_markup=markup_big)
#
#
# @dp.message_handler(commands='rm')
# async def func_rm(message: types.Message):
#     await message.reply('rm', reply_markup=ReplyKeyboardRemove())

inline_btn1 = InlineKeyboardButton('Первая кнопка', callback_data='button1')

inline_kb1 = InlineKeyboardMarkup().add(inline_btn1)


@dp.message_handler(commands=['1', '2', '10'])
async def func_inline(message: types.Message):
    await message.reply('Первая кнопка', reply_markup=inline_kb1)


@dp.callback_query_handler(Text(equals='button1'))
async def func_callback(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, 'Нажата первая кнопка')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
