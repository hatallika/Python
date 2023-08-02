from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboard.inline.callback_datas import url_callback
from keyboard.inline.choice_button import choice, google_keyboard, yandex_keyboard
from loader import dp


@dp.message_handler(Command('items'))
async def show_item(message: Message):
    await message.answer(text='Здравствуйте, выберите необходимую ссылку', reply_markup=choice)


@dp.callback_query_handler(text_contains='google')
async def get_google_url(call: CallbackQuery):
    await call.answer(cache_time=10)
    await call.message.answer('Вы выбрали google', reply_markup=google_keyboard)


# @dp.callback_query_handler(text_contains='yandex')
# async def get_yandex_url(call: CallbackQuery):
#     await call.answer(cache_time=10)
#     await call.message.answer('Вы выбрали yandex', reply_markup=yandex_keyboard)

@dp.callback_query_handler(url_callback.filter(item_name='yandex'))
async def get_yandex_url(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=10)
    print(callback_data)
    await call.message.answer('Вы выбрали yandex', reply_markup=yandex_keyboard)


@dp.callback_query_handler(text='cancel')
async def cancel_bot(call: CallbackQuery):
    await call.answer('Вы нажали отмену')
    # убрали клавиатуру
    await call.message.edit_reply_markup(reply_markup=None)
