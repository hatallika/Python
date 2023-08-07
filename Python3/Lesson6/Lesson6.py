import os
from dotenv import load_dotenv
import logging
import datetime
from typing import Dict
from aiogram import Bot, Dispatcher, executor, types
from inlinetime.inlinetime import Time

load_dotenv()
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('aiogram').setLevel(logging.INFO)

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

inline_time = Time()


@dp.message_handler(commands=['time'])
async def start_time(message: types.Message):
    inline_time.init(
        datetime.time(12),
        datetime.time(1),
        datetime.time(23),
    )
    await bot.send_message(message.from_user.id,
                           text='test',
                           reply_markup=inline_time.get_keyboard())


@dp.callback_query_handler(inline_time.filter())
async def cb_handler(query: types.CallbackQuery, callback_data: Dict[str, str]):
    await query.answer()  # сброс часиков - ожидания ответа

    handle_result = inline_time.handle(query.from_user.id, callback_data)

    if handle_result is not None:
        await bot.edit_message_text(handle_result,
                                    chat_id=query.from_user.id,
                                    message_id=query.message.message_id)
    else:
        await bot.edit_message_reply_markup(chat_id=query.from_user.id,
                                            message_id=query.message.message_id,
                                            reply_markup=inline_time.get_keyboard())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
