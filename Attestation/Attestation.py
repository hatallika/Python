# Аттестация
# Реализовать бота интернет магазина товаров.
# Бот должен иметь функционал регистрации пользователей,
# содержать инлайн клавиатуру, меню,
# использовать систему платежей,
# возможность указать тип доставки

import os
import Product

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

ADMIN_ID = os.getenv('ADMIN_ID')
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
cb_category = CallbackData("category", "name")

# Главное меню
menu_keyboard = InlineKeyboardMarkup(row_width=1)
button_catalog = InlineKeyboardButton('Каталог', callback_data=cb_menu.new(name='catalog'))
button_registration = InlineKeyboardButton('Регистрация', callback_data=cb_menu.new(name='reg'))
button_help = InlineKeyboardButton('Помощь', callback_data=cb_menu.new(name='help'))
menu_keyboard.add(button_catalog).add(button_registration).add(button_help)

# Клавиатура c Категориями товаров
category_keyboard = ReplyKeyboardMarkup()
category_list = db.get_categories()
for category in category_list:
    (category,) = category
    category_keyboard.add(KeyboardButton(category))
category_keyboard.add(KeyboardButton('Назад'))


# Если админ магазина (владелец бота)
class AdminFilter(BoundFilter):
    async def check(self, message: types.Message):
        # проверим кто отправитель сообщения
        member = await message.chat.get_member(message.from_user.id)
        return member.user.id == int(ADMIN_ID)


class AwaitRegisterData(StatesGroup):
    fio_add = State()
    phone_add = State()
    register_finish = State()


# параметры доставки
# доставка курьером
POST_FAST_SHIPPING = types.ShippingOption(
    id='post_fast',
    title='Курьер',
    prices=[
        types.LabeledPrice(
            'Заводская упаковка', 0
        ),
        types.LabeledPrice(
            'Курьер', 490_00
        )
    ]
)

# Самовывоз
PICKUP_SHIPPING = types.ShippingOption(
    id='pickup',
    title='Самовывоз',
    prices=[
        types.LabeledPrice(
            'Самовывоз из магазина', 0
        )
    ]
)


@dp.message_handler(CommandStart())
async def start_bot(message: types.Message):
    await message.answer('Добро пожаловать в магазин\nМеню', reply_markup=menu_keyboard)
    # # Создали бд
    # try:
    #     db.create_table_products()
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
    text = ""
    for user_id, username in users:
        text += f'{user_id} {username}\n'
    await bot.send_message(message.from_user.id, text)


@dp.callback_query_handler(cb_menu.filter(name=['catalog']))
async def get_catalog(call: types.CallbackQuery):
    await call.message.answer('Выберите категорию товара', reply_markup=category_keyboard)


# Получили команды при выборе категорий
@dp.message_handler(text=[''.join(data) for data in category_list])
async def get_products(message: types.Message):
    category_ = message.text
    products = db.get_products(category_)

    try:
        # Получим список карточек
        for item in products:
            # (id, title, category, description, price, discount, img_url) = item
            keys = ('id', 'title', 'category', 'description', 'price', 'discount', 'img_url')
            # получили словарь
            dictionary = dict(zip(keys, item))
            print(dictionary)  # {'a': 1, 'b': 2, 'c': 3}
            card = Product.get_product_class_item(dictionary, '1')
            await bot.send_invoice(message.from_user.id, **card.generate_invoice(), payload='123456')
    except Exception as err:
        print(err)


@dp.shipping_query_handler()
async def choice_shipping(query: types.ShippingQuery):
    # проверим адрес доставки
    if query.shipping_address.country_code == 'RU':
        # вернем варианты доставки
        await bot.answer_shipping_query(shipping_options=[
            POST_FAST_SHIPPING,
            PICKUP_SHIPPING
        ], shipping_query_id=query.id, ok=True)
    else:
        # вернем варианты доставки (нет)
        await bot.answer_shipping_query(shipping_query_id=query.id, ok=False,
                                        error_message='Доставки в данный регион нет')


@dp.message_handler(text='Назад к Меню')
async def back_to_menu(message: types.Message):
    await message.answer('Меню магазина', reply_markup=menu_keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
