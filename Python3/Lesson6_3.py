# Клавиатуры в Telegram (3)
import os
import logging

from aiogram.dispatcher.filters import CommandStart
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

load_dotenv()
TOKEN = os.getenv('TOKEN')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Создадим кнопки
button1 = KeyboardButton('Категории')
button2 = KeyboardButton('Помощь')
button3 = KeyboardButton('Отзывы')


# Клавиатура inline
youtube_butt = InlineKeyboardButton('Youtube', callback_data='youtube_kb')
gamepass_butt = InlineKeyboardButton('Game Pass', callback_data='gamepass_kb')
playstation_butt = InlineKeyboardButton('Playstation', callback_data='playstation_kb')
back = InlineKeyboardButton('Назад', callback_data='back')

# Клавиатура
start_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
start_kb.row(button1, button2)
start_kb.row(button3)

inline_kb = InlineKeyboardMarkup().add(gamepass_butt, playstation_butt, youtube_butt)
inline_kb.add(back)

button_back = KeyboardButton('Назад')
back_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_back)

youtube_t1 = InlineKeyboardButton('Youtube Premium 1 мес', callback_data='youtube_t1')
youtube_t2 = InlineKeyboardButton('Youtube Premium 6 мес', callback_data='youtube_t2')
youtube_back = InlineKeyboardButton('Назад', callback_data='youtube_back')
youtube_back_cat = InlineKeyboardButton('Вернуться к категориям', callback_data='youtube_back_cat')

youtube_kb1 = InlineKeyboardMarkup()
youtube_kb1.add(youtube_t1)
youtube_kb1.add(youtube_t2)
youtube_kb1.add(youtube_back)
youtube_kb1.add(youtube_back_cat)

#  Game Pass
gamepass_t1 = InlineKeyboardButton('Game Pass Premium 1 мес', callback_data='gamepass_t1')
gamepass_t2 = InlineKeyboardButton('Game Pass Premium 6 мес', callback_data='gamepass_t2')
gamepass_back = InlineKeyboardButton('Назад', callback_data='gamepass_back')
gamepass_back_cat = InlineKeyboardButton('Вернуться к категориям', callback_data='gamepass_back_cat')

gamepass_kb1 = InlineKeyboardMarkup()
gamepass_kb1.add(gamepass_t1)
gamepass_kb1.add(gamepass_t2)
gamepass_kb1.add(gamepass_back)
gamepass_kb1.add(gamepass_back_cat)

# PlayStation
playstation_t1 = InlineKeyboardButton('PS + 1 мес', callback_data='playstation_t1')
playstation_t2 = InlineKeyboardButton('PS + 6 мес', callback_data='playstation_t2')
playstation_back = InlineKeyboardButton('Назад', callback_data='playstation_back')
playstation_back_cat = InlineKeyboardButton('Вернуться к категориям', callback_data='playstation_back_cat')

playstation_kb1 = InlineKeyboardMarkup()
playstation_kb1.add(playstation_t1)
playstation_kb1.add(playstation_t2)
playstation_kb1.add(playstation_back)
playstation_kb1.add(playstation_back_cat)


# принимаем все data_callback
@dp.callback_query_handler()
async def chec_cat(call: types.CallbackQuery):
    if call.data == 'youtube_kb':
        await call.message.delete()
        await call.message.answer('Какую подписку хотите выбрать', reply_markup=youtube_kb1)
    elif call.data == 'gamepass_kb':
        await call.message.delete()
        await call.message.answer('Какую подписку хотите выбрать', reply_markup=gamepass_kb1)
    elif call.data == 'playstation_kb':
        await call.message.delete()
        await call.message.answer('Какую подписку хотите выбрать', reply_markup=playstation_kb1)
    elif call.data == 'youtube_t1':
        await call.message.delete()
        await call.message.answer('Вы хотите купить подписку на 1 месяц')
    elif call.data == 'youtube_t2':
        await call.message.delete()
        await call.message.answer('Вы хотите купить подписку на 6 месяцев')
    elif call.data == 'gamepass_t1':
        await call.message.delete()
        await call.message.answer('Вы хотите купить подписку на 1 месяц')
    elif call.data == 'gamepass_t2':
        await call.message.delete()
        await call.message.answer('Вы хотите купить подписку на 6 месяцев')
    elif call.data == 'playstation_t1':
        await call.message.delete()
        await call.message.answer('Вы хотите купить подписку на 1 месяц')
    elif call.data == 'playstation_t2':
        await call.message.delete()
        await call.message.answer('Вы хотите купить подписку на 6 месяцев')
    elif call.data == 'youtube_back':
        await call.message.delete()
        await call.message.answer('Вы вернулись назад', reply_markup=youtube_kb1)
    elif call.data == 'gamepass_back':
        await call.message.delete()
        await call.message.answer('Вы вернулись назад', reply_markup=gamepass_kb1)
    elif call.data == 'playstation_back':
        await call.message.delete()
        await call.message.answer('Вы вернулись назад', reply_markup=playstation_kb1)
    elif call.data == 'youtube_back_cat':
        await call.message.delete()
        await call.message.answer('Вы вернулись к категориям', reply_markup=inline_kb)
    elif call.data == 'gamepass_back_cat':
        await call.message.delete()
        await call.message.answer('Вы вернулись к категориям', reply_markup=inline_kb)
    elif call.data == 'playstation_back_cat':
        await call.message.delete()
        await call.message.answer('Вы вернулись к категориям', reply_markup=inline_kb)
    elif call.data == 'back':
        await call.message.delete()
        await call.message.answer('Вы вернулись назад', reply_markup=start_kb)



@dp.message_handler(text='Помощь')
async def func_help(message: types.Message):
    await message.answer('У вас ошибка? Напишите администратору', reply_markup=back_kb)


@dp.message_handler(text='Отзывы')
async def func_review(message: types.Message):
    await message.answer('На текущий момент раздел в разработке', reply_markup=back_kb)


@dp.message_handler(text='Назад')
async def func_back(message: types.Message):
    await message.answer('Вы вернулись в главное меню', reply_markup=start_kb)


@dp.message_handler(CommandStart())
async def start_command(message: types.Message):
    await message.answer('Привет, вы вошли в магазин', reply_markup=start_kb)


@dp.message_handler(text='Категории')
async def get_category(message: types.Message):
    await message.answer('Вы вошли в Категории', reply_markup=inline_kb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
