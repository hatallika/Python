import logging
import os

import requests
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
# Для оформления
import aiogram.utils.markdown as fmt
from db import Database
import config

load_dotenv()

TOKEN = os.getenv('TOKEN')
db = Database('db.db')
logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN, parse_mode='html')
dp = Dispatcher(bot)


# проверка на подписку на наш канал
def check_sub_channel(chat_member):
    print(chat_member['status'])
    if chat_member['status'] != 'left':
        return True
    return False


# лучше хранить в окружении!
admins = [112112, 212118900]


@dp.message_handler(content_types=['left_chat_members'])
async def left(message: types.Message):
    print(message.from_user.id)


# проверка
@dp.message_handler(content_types=['new_chat_members'])
async def start(message: types.Message):
    print(message.from_user.id)
    # if check_sub_channel(await bot.get_chat_member(chat_id=config.channel_id, user_id=message.from_user.id)):
    #     db.add_user(message.from_user.id)
    #     await bot.send_message(message.from_user.id, 'LOG BOT RESTART')
    #     await message.answer('<b>Привет</b> Я новый бот-модератор вашего канала')
    # else:
    #     await bot.send_message(message.from_user.id, 'Вы не подписаны')


# рассылка
@dp.message_handler(commands='send_all')
async def send_all(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=config.channel_id, user_id=message.from_user.id)):
        # если админ
        if message.from_user.id == config.admin:
            text = message.text[9:]
            users = db.get_users()
            for row in users:
                try:
                    await bot.send_message(row[0], text)
                    if int(row[1]) != 1:
                        db.set_active(row[0], 1)
                except Exception as err:
                    print(err)
                    db.set_active(row[0], 0)
            await bot.send_message(message.from_user.id, 'Успешная рассылка ')
        else:
            await message.reply('У вас недостаточно прав')
    else:
        await message.reply('Вы не подписаны на канал')


@dp.message_handler(commands='ban')
async def ban_user(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=config.channel_id, user_id=message.from_user.id)):
        if message.from_user.id == config.admin:
            # ???? (в канале так же?)
            # await message.bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            await message.bot.ban_chat_member(chat_id=config.channel_id, user_id=message.from_user.id)
            await message.answer(f'Пользователь {message.from_user.full_name} забанен')
        else:
            await message.reply('У вас недостаточно прав')
    else:
        await message.reply('Вы не подписаны на канал')


@dp.message_handler(commands='unban')
async def ban_user(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=config.channel_id, user_id=message.from_user.id)):
        if message.from_user.id == config.admin:
            # ???? (в канале так же?)
            await message.bot.unban_chat_member(chat_id=config.channel_id, user_id=message.from_user.id)
            await message.answer(f'Пользователь {message.from_user.full_name} разбанен')
        else:
            await message.reply('У вас недостаточно прав')
    else:
        await message.reply('Вы не подписаны на канал')


# Отклик бота
@dp.message_handler(commands='bot')
async def ban_user(message: types.Message):
    print('Hey')
    if check_sub_channel(await bot.get_chat_member(chat_id=config.channel_id, user_id=message.from_user.id)):
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
            await message.answer('Да да, я тут')
    else:
        await message.reply('Вы не подписаны на канал')


# Вывод правил
@dp.message_handler(commands='set_rules')
async def ban_user(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=config.channel_id, user_id=message.from_user.id)):
        if message.from_user.id == config.admin:
            config.rules = message.text[11:]
            await message.answer(f'Правила в чате установлены {config.rules}')
        else:
            await message.reply('У вас недостаточно прав')
    else:
        await message.reply('Вы не подписаны на канал')


@dp.message_handler(commands='rules')
async def ban_user(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=config.channel_id, user_id=message.from_user.id)):
        await message.answer(f'{config.rules}')
    else:
        await message.reply('Вы не подписаны на канал')


# Вывести id
@dp.message_handler(commands='get_my_id')
async def my_id(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=config.channel_id, user_id=message.from_user.id)):
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
        await message.answer(f'Твой id {message.from_user.id}')

    else:
        await message.reply('Вы не подписаны на канал')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
