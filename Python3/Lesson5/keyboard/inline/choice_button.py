from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import URL_GOOGLE, URL_YANDEX
from keyboard.inline.callback_datas import url_callback

choice = InlineKeyboardMarkup(row_width=2)
url_google = InlineKeyboardButton(text='Google', callback_data=url_callback.new(item_name='google'))
url_yandex = InlineKeyboardButton(text='Yandex', callback_data=url_callback.new(item_name='yandex'))
cancel =InlineKeyboardButton(text='Отмена', callback_data='cancel')

choice.insert(url_google)
choice.insert(url_yandex)
choice.insert(cancel)

google_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Ссылка', url=URL_GOOGLE)
    ],
])

yandex_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Ссылка', url=URL_YANDEX)
    ],
])