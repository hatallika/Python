# Домашнее задание:
# Реализация ограничения доступа в чат боте#
# Планируемый результат:#
# Готовая реализация по ограничению доступа

# Решение: Реализуем программу, где администратор группы, может сделать определенное количество предупреждений пользователю
# После превышения количества предупреждений пользователь удаляется из группы (бан/кик).

import os
import datetime

from aiogram.dispatcher.filters import BoundFilter
from dotenv import load_dotenv
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command, CommandStart, Text

load_dotenv()

TOKEN = os.getenv('TOKEN')
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot)


# Фильтры для ограничения команд
# Если админ
class AdminFilter(BoundFilter):
    async def check(self, message: types.Message):
        # проверим кто отправитель сообщения
        member = await message.chat.get_member(message.from_user.id)
        return member.is_chat_admin()


# Разрешено в группе
class isGroup(BoundFilter):
    # Написано в группе или нет
    async def check(self, message: types.Message):
        return message.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPERGROUP
        )


# страйк лист
attempt = 3
strike_list = {}


@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.answer('Hello!')


# Применнение фильтров: отправка предупреждения пользователю
@dp.message_handler(isGroup(), Command('strike', prefixes='/!'), AdminFilter())
async def set_new_photo(message: types.Message):
    # исходное сообщение
    source_message = message.reply_to_message
    # получим данные из сообщения пользователя
    user = source_message.from_user
    print(user.id)
    count = strike_list.get(user.id, 0)
    strike_list[user.id] = count + 1
    print(strike_list)
    if strike_list[user.id] < attempt:
        # Предупреждение
        await message.answer(
            f'Предупреждение пользователю {user.get_mention(as_html=True)} {strike_list[user.id]} из ({attempt})')
    else:
        await message.chat.kick(user_id=user.id, until_date=datetime.datetime.now() + datetime.timedelta(seconds=15))
        # await bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id, 5)
        await message.reply(f'Пользователь {user.get_mention()} kick на 15 секунд')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
