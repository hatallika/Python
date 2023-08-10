from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

import os
from dotenv import load_dotenv
load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class AwaitMessages(StatesGroup):
    fio_add = State()
    phone_add = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет, давай зарегистрируемся')
    await AwaitMessages.fio_add.set()

@dp.message_handler(state=AwaitMessages.fio_add)
async def process_fio_add(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fio'] = message.text
    # зачем?
    # await state.finish()
    # нет смысла юзать bot.send_message если вы отправляете в этот же чат
    # await bot.send_message(message.chat.id, 'Введите телефон: ')
    await message.answer('Введите телефон.')
    await AwaitMessages.phone_add.set()


@dp.message_handler(state=AwaitMessages.phone_add)
async def process_fio_add(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
        await message.answer(f'ФИО - {data["fio"]}\nНомер - {data["phone"]}')
        await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
