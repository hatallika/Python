# Реализовать бота интернет магазина товаров.
# Бот должен иметь функционал регистрации пользователей,
# содержать инлайн клавиатуру, меню,
# использовать систему платежей,
# возможность указать тип доставки
# 1111 1111 1111 1026, 12/22, CVC 000.
import os

from aiogram.utils.callback_data import CallbackData
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import CommandStart, BoundFilter, Command
import logging
from DataBase import Database

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database('shop.db')

# Логирование
logging.basicConfig(level=logging.INFO)

# Keyboards
contact_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    KeyboardButton('Поделиться контактом', request_contact=True))
cb_menu = CallbackData("menu", "name")

menu_keyboard = InlineKeyboardMarkup(row_width=1)

button_catalog = InlineKeyboardButton('Каталог', callback_data=cb_menu.new(name='catalog'))
button_registration = InlineKeyboardButton('Регистрация', callback_data=cb_menu.new(name='reg'))
button_help = InlineKeyboardButton('Помощь', callback_data=cb_menu.new(name='help'))

menu_keyboard.add(button_catalog).add(button_registration).add(button_help)


# Если админ магазина (владелец бота)
class AdminFilter(BoundFilter):
    async def check(self, message: types.Message):
        # проверим кто отправитель сообщения
        member = await message.chat.get_member(message.from_user.id)
        print(member)
        return member.user.id == 426556664


class AwaitRegisterData(StatesGroup):
    fio_add = State()
    phone_add = State()
    register_finish = State()


@dp.message_handler(CommandStart())
async def start_bot(message: types.Message):
    await message.answer('Добро пожаловать в магазин\nМеню', reply_markup=menu_keyboard)
    # # Создали бд
    # try:
    #     db.create_table()
    # except Exception as err:
    #     print(err)


@dp.callback_query_handler(cb_menu.filter(name=['reg']))
async def start(call: types.CallbackQuery):
    try:
        print(call.from_user.id, db.user_exists(call.message.from_user.id))
        if db.user_exists(call.from_user.id):
            await call.message.answer('Вы уже зарегистрированы')
        else:
            await call.message.answer('Напишите ваше ФИО')
            await AwaitRegisterData.fio_add.set()
    except Exception as err:
        print(err)


@dp.message_handler(state=AwaitRegisterData.fio_add)
async def process_fio_add(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        customer = message.from_user
        data['username_id'] = customer.id
        data['username'] = customer.username
        data['fullname'] = message.text
    # Нельзя использовать получение контакта в открытой группе. (Регистрация проводится напрямую человек - бот)
    await message.answer('Отправьте контакт или введите номер вручную.', reply_markup=contact_keyboard)
    await AwaitRegisterData.phone_add.set()


@dp.message_handler(content_types=[types.ContentType.CONTACT, types.ContentType.TEXT],
                    state=AwaitRegisterData.phone_add)
async def process_fio_add(message: types.Message, state: FSMContext):
    customer = message.from_user
    # клиент ввел номер вручную или поделился контактом:
    async with state.proxy() as data:
        if message.contact is not None:
            data['phone'] = message.contact.phone_number
        else:
            data['phone'] = message.text
            # Здесь можно добавить проверку номера телефона на валидность

        await message.answer(f'Спасибо за регистрацию. Ваши данные\nФИО - {data["fullname"]}\nНомер - {data["phone"]}')
        await message.answer('Меню', reply_markup=menu_keyboard)

    # Отправили в базу данных
    db.add_user(user_id=customer.id, username=customer.username, fullname=data["fullname"], phone=data["phone"])
    await state.finish()


@dp.message_handler(AdminFilter(), Command('get_users'))
async def get_users(message: types.Message):
    users = db.get_users_id()
    print(users)
    text = ""
    for user_id, username in users:
        text += f'{user_id} {username}\n'
    await bot.send_message(message.from_user.id, text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
