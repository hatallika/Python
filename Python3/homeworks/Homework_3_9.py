# Домашнее задание
# Реализация и подключение системы платежей к боту
# Планируемый результат:#

# Готовая реализация системы платежей
# Решение, подключим PayMaster к магазину товаров

import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from dataclasses import dataclass
from aiogram.types import LabeledPrice
from typing import List
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

load_dotenv()
# предполагаемая БД
products = [
    {
        'id': 1,
        'category': 'Молочные продукты',
        'description': 'Поставщик: Вкусняево',
        'title': 'Молоко, 1л',
        'price': 78_00,
        'discount': -10,
        'img_url': 'https://main-cdn.sbermegamarket.ru/big1/hlr-system/-13/500/762/431/216/223/3/100045569106b0.jpg'
    },
    {
        'id': 2,
        'category': 'Молочные продукты',
        'description': 'Изготовлено из 100% натуральных продуктов',
        'title': 'Сыр сливочный, 200г',
        'price': 250_00,
        'discount': -10,
        'img_url': 'https://storum.ru/image/cache/products/330194-800x800.jpg'
    },
    {
        'id': 3,
        'category': 'Кондитерские изделия',
        'description': 'Фабрика Красный октябрь',
        'title': 'Конфеты Рафаэлло, 150г',
        'price': 650_00,
        'discount': -10,
        'img_url': 'https://www.beauty-flowers-moscow.ru/wp-content/uploads/2018/03/konfety-raffaello-150g.jpg'
    },
    {
        'id': 4,
        'category': 'Кондитерские изделия',
        'description': 'Фабрика Красный октябрь',
        'title': 'Шоколад Аленка, 100г',
        'price': 78_00,
        'discount': -10,
        'img_url': 'https://www.alenka.ru/upload/iblock/3ae/3ae597cbf0687f64294bb43341ee1852.jpg'
    }
]

TOKEN = os.getenv('TOKEN')
PAYMENT_TOKEN = os.getenv('PAYMENT_TOKEN')
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('aiogram').setLevel(logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dataclass
class Product:
    title: str
    description: str
    start_parameter: str
    currency: str
    prices: List[LabeledPrice]
    provider_data: dict = None
    photo_url: str = None
    photo_size: int = None
    photo_width: int = None
    photo_height: int = None
    need_name: bool = False
    need_phone_number: bool = False
    need_email: bool = False
    need_shipping_address: bool = False
    send_phone_number_to_provider: bool = False
    send_email_to_provider: bool = False
    is_flexible: bool = False
    provider_token: str = PAYMENT_TOKEN

    def generate_invoice(self):
        return self.__dict__


def get_product_class_item(product: dict):
    return Product(
        title=product['title'],
        description=product['description'],
        currency='RUB',
        prices=[
            LabeledPrice(
                label=product['title'],
                amount=product['price']
            ),
            LabeledPrice(
                label='Скидка',
                amount=product['discount']
            )
        ],
        start_parameter='create_invoice_product',
        photo_url=product['img_url'],
        photo_size=600,
        need_shipping_address=True,
        is_flexible=True
    )


# Создадим список классов Product
product_list = []
for product in products:
    class_item = get_product_class_item(product)
    product_list.append(class_item)

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


@dp.message_handler(Command('products'))
async def show_invoices(message: types.Message):
    for item in product_list:
        await bot.send_invoice(message.from_user.id, **item.generate_invoice(), payload='123456')


@dp.shipping_query_handler
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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
