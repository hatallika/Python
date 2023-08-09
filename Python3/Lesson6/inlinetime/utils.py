from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


def create_button(text):
    return KeyboardButton(text=text)


def create_keyboard(*buttons, row_width=3, one_time_keyboard=True):
    nk = ReplyKeyboardMarkup(row_width=row_width,
                             one_time_keyboard=True,
                             resize_keyboard=True)
    nk.add(*buttons)
    return nk


def create_inline_callback_button(text, callback_data):
    return InlineKeyboardButton(text=text, callback_data=callback_data)


# генератор кнопок
def create_inline_callback_buttons(list):
    for text, callback in list:
        yield create_inline_callback_button(text, callback)


def create_inline_keyboard(*buttons, row_width=3):
    nk = InlineKeyboardMarkup(row_width=row_width)
    nk.add(*buttons)
    return nk
