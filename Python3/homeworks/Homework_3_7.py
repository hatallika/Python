# Домашнее задание:
# Реализация меню для чат бота#
# Планируемый результат:#
# Готовое меню для чат бота согласно условиям

import os
import logging

from aiogram.dispatcher.filters import CommandStart, BoundFilter
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData

load_dotenv()
TOKEN = os.getenv('TOKEN')
logging.basicConfig(level=logging.INFO)

print(TOKEN)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

products = [
    {
        'id': 1,
        'category': 'Молочные продукты',
        'title': 'Молоко, 1л',
        'price': '78.00'
    },
    {
        'id': 2,
        'category': 'Молочные продукты',
        'title': 'Сыр сливочный, 180г',
        'price': '250.00'
    },
    {
        'id': 3,
        'category': 'Кондитерские изделия',
        'title': 'Конфеты Рафаэлло, 180г',
        'price': '650.00'
    },
    {
        'id': 4,
        'category': 'Кондитерские изделия',
        'title': 'Шоколад Аленка, 100г',
        'price': '78.00'
    }
]


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Начало работы'),
        types.BotCommand('get_menu', 'Открыть меню'),
    ])

# Создадим кнопки главного меню
button1 = KeyboardButton('Категории')
button2 = KeyboardButton('Помощь')
button3 = KeyboardButton('О компании')
button4 = KeyboardButton('Отзывы')

menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
menu_kb.row(button1, button2, button3, button4)

# кнопка назад для категорий
back = InlineKeyboardButton('Назад', callback_data='back')

cb_product = CallbackData("product_cb", "name", "id")
cb_cat = CallbackData("category_cb", "name")


# Клавиатуры для каждой категории списка
def get_keyboard(category: str):
    kb_ = InlineKeyboardMarkup()
    for pr in products:
        if pr['category'] == category:
            # Добавили кнопки с товарами из категории
            kb_.insert(InlineKeyboardButton(text=f'{pr["id"]} {pr["title"]}',
                                            callback_data=cb_product.new(name=pr["title"], id=pr["id"])))
    kb_.row(back)
    return kb_


# Получим список клавиатур по категориям
cat_kb_list = {}
for product in products:
    if product['category'] not in cat_kb_list:
        kb = get_keyboard(product['category'])
        cat_kb_list[product['category']] = kb

category_kb = InlineKeyboardMarkup()
for item in cat_kb_list:
    button = InlineKeyboardButton(item, callback_data=cb_cat.new(name=item))
    category_kb.insert(button)


@dp.message_handler(CommandStart())
async def start_menu(message: types.Message):
    await message.answer('Меню', reply_markup=menu_kb)


@dp.message_handler(text='Категории')
async def get_all_categories(message: types.Message):
    await message.answer('Категории', reply_markup=category_kb)


@dp.callback_query_handler(cb_cat.filter())
async def get_category_products(call: types.CallbackQuery, callback_data: dict):
    category = callback_data['name']
    await call.message.edit_text(text=category, reply_markup=cat_kb_list[category])


@dp.callback_query_handler(text='back')
async def back(call: types.CallbackQuery):
    await call.message.edit_text('Категории', reply_markup=category_kb)


@dp.callback_query_handler(cb_product.filter())
async def get_product_info(call: types.CallbackQuery, callback_data: dict):
    title = callback_data['name']
    product_id = callback_data['id']
    price = [product_['price'] for product_ in products if product_['id'] == int(product_id)]

    await call.message.edit_text(text=f'{title}\nЦена: {price[0]}')


@dp.message_handler(text=['О компании', 'Помощь', 'Отзывы'])
async def get_answer(message: types.Message):
    await message.answer('Раздел находится в разработке')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
