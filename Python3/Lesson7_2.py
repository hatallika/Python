import asyncio
import io
import logging
import os
import datetime
from abc import ABC

from dotenv import load_dotenv
import re
from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Command, CommandStart, BoundFilter
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.contrib.fsm_storage.redis import RedisStorage
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import BadRequest

load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN, parse_mode='html')

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Бот сработает на любую команду и в чате и в группе, куда он добавлен
# @dp.message_handler()
# async def test(message: types.Message):
#     await message.answer('Привет, я бот')

async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands([
        types.BotCommand('set_photo', 'Установить фото в группе'),
        types.BotCommand('set_title', 'Установить название группы'),
        types.BotCommand('set_description', 'Установить описание группы'),
        types.BotCommand('ro', 'Режим Read Only'),
        types.BotCommand('unro', 'Отключить RO'),
        types.BotCommand('ban', 'Забанить пользователя'),
        types.BotCommand('unban', 'Разбанить пользователя')
    ])


# Приветствие новых пользователей
@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_member(message: types.Message):
    members = ', '.join(m.get_mention(as_html=True) for m in message.new_chat_members)
    await message.reply(f'Привет, {members}')


# Исключение пользовтелей
@dp.message_handler(content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def banned_member(message: types.Message):
    # если пользователь удалился по своей инициативе
    if message.left_chat_member.id == message.from_user.id:
        await message.answer(f'Пользователь {message.left_chat_member.get_mention(as_html=True)} вышел из чата')
        # где get_mention выводит ссылку на пользователя
    # пользователь я
    elif message.from_user.id == (await bot.me).id:
        return
    # пользователя удалил администратор
    else:
        await message.reply(
            f'{message.left_chat_member.full_name} был удален из чата {message.from_user.get_mention(as_html=True)}')


class AdminFilter(BoundFilter):
    async def check(self, message: types.Message):
        # проверим кто отправитьель сообщения
        member = await message.chat.get_member(message.from_user.id)
        return member.is_chat_admin()


class isGroup(BoundFilter):
    # Написано в группе или нет
    async def check(self, message: types.Message):
        return message.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPERGROUP
        )


# Применнение фильтров: при изменении фото проверять а группа ли это
@dp.message_handler(isGroup(), Command('set_photo', prefixes='/!'), AdminFilter())
async def set_new_photo(message: types.Message):
    # исходное сообщение
    source_message = message.reply_to_message
    # получим фото из сообщения
    photo = source_message.photo[-1]
    # загрузить фото
    photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(path_or_bytesio=photo)
    await message.chat.set_photo(photo=input_file)


# Установка названия группы
@dp.message_handler(isGroup(), Command('set_title', prefixes='!/'), AdminFilter())
async def set_new_title(message: types.Message):
    source_message = message.reply_to_message
    title = source_message.text
    await message.chat.set_title(title=title)


# Установка описания группы
@dp.message_handler(isGroup(), Command('set_description', prefixes='!'), AdminFilter())
async def set_new_description(message: types.Message):
    source_message = message.reply_to_message
    description = source_message.text
    await message.chat.set_description(description=description)


@dp.message_handler(isGroup(), Command('ban', prefixes='!/'), AdminFilter())
async def ban_user(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    await message.chat.kick(user_id=member_id)
    await message.reply(f'Пользователь {member.full_name} был удален из чата')
    # сделаем чтобы сообщение пропало
    service_message = await message.reply('Сообщение удалится через 5 секунд')
    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()


@dp.message_handler(isGroup(), Command('unban', prefixes='!/'), AdminFilter())
async def unban_user(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    print(member_id)
    await message.chat.unban(user_id=member_id)
    await message.reply(f'Пользователь {member.full_name} был разбанен')
    services_message = await message.reply('Сообщение удалится через 5 секунд')
    await asyncio.sleep(5)
    await message.delete()
    await services_message.delete()


@dp.message_handler(isGroup(), Command('ro', prefixes='!/'), AdminFilter())
async def read_only_user(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    # Регулярное выражение: Команда, время бана, причина бана
    command_parse = re.compile(r'(!ro|/ro) ? (\d+)? ?([a-zA-Z])+?')
    # парсим сообщение администратора
    parsed = command_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)
    if not time:
        time = 5
    else:
        time = int(time)

    # через сколько будет разбанен
    until_date = datetime.datetime.now() - datetime.timedelta(minutes=time)
    # ограничения чата
    ReadOnlyPermission = types.ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_polls=False,
        can_invite_users=True,
        can_pin_messages=False,
        can_change_info=False,
        can_add_web_page_previews=False
    )
    try:
        print(chat_id, member_id, until_date)
        await bot.restrict_chat_member(chat_id, user_id=member_id, permissions=ReadOnlyPermission,
                                       until_date=until_date)
        await message.answer(
            f'Пользователю {member.get_mention(as_html=True)} запрещено писать на {time} минут по причине: {comment}')
    except BadRequest as err:
        await message.answer(f'Пользователь {member.get_mention(as_html=True)}является администратором, {err}')
        service_message = await message.reply('Сообщение уадлится через 5 секунд')
        await asyncio.sleep(5)
        await message.delete()
        await service_message.delete()

    # !ro 5 флуд


@dp.message_handler(isGroup(), Command('unro', prefixes='/!'), AdminFilter())
async def unro_user(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    User_Allowed = types.ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_invite_users=True,
        can_pin_messages=True,
        can_change_info=True,
        can_add_web_page_previews=True
    )
    try:
        await message.chat.restrict(user_id=member_id, permissions=User_Allowed, until_date=0)
        await message.reply(f'Пользователь {member.get_mention()} был разбанен')
        service_message = await message.reply('Сообщение уадлится через 5 секунд')
        await asyncio.sleep(5)
        await message.delete()
        await service_message.delete()
    except BadRequest as err:
        await message.answer(err)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
