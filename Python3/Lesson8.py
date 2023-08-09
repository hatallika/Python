# payment Система платежей (в уроке по ограничению доступа)

import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from dataclasses import dataclass
from aiogram.types import LabeledPrice
from typing import List
from aiogram.dispatcher.filters import Command

load_dotenv()

TOKEN = os.getenv('TOKEN')
PAYMENT_TOKEN = os.getenv('PAYMENT_TOKEN')
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('aiogram').setLevel(logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# продажа ноутбуков

@dataclass
class Item:
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


NoteBook = Item(
    title='Ноутбук Lenovo IP Gaming 3',
    description='Ноутбук Lenovo IdeaPad Gaming 3 15IMH05 включает в себя 15.6-дюймовый экран, основу которого составила'
                ' матрица IPS, позволяющая вам насладиться невероятной четкостью и детализацией каждой картинки. ',
    currency='RUB',
    prices=[
        LabeledPrice(
            label='Ноутбук Lenovo IP Gaming 3',
            amount=40_000_00
        ),
        LabeledPrice(
            label='Доставка',
            amount=500_00
        ),
        LabeledPrice(
            label='Скидка',
            amount=-2_000_00
        )
    ],
    start_parameter='create_invoice_notebook_Lenovo',
    photo_url='https://c.dns-shop.ru/thumb/st4/fit/500/500/ca59f0087d33d5cbbf8d7a93ce157c74/63add0435dc2ca1f4082d79c725ff635bf24115760a1825efa496a176cf2d807.jpg',
    photo_size=600,
    need_shipping_address=True,
    is_flexible=True
)
# доставка почтой
POST_REGULAR_SHIPPING = types.ShippingOption(
    id='post_reg',
    title='Почтой',
    prices=[
        types.LabeledPrice(
            'Заводская упаковка', 0
        ),
        types.LabeledPrice(
            'Почтой', 200_00
        )
    ]
)
# доставка курьером
POST_FAST_SHIPPING = types.ShippingOption(
    id='post_fast',
    title='Курьер',
    prices=[
        types.LabeledPrice(
            'Заводская упаковка', 0
        ),
        types.LabeledPrice(
            'Курьер', 500_00
        )
    ]

)
# Самовывоз
PICKUP_SHIPPING = types.ShippingOption(
    id='pickup',
    title='Самовывоз',
    prices=[
        types.LabeledPrice(
            'Самовывоз из магазина', -200
        )
    ]
)


@dp.message_handler(Command('invoices'))
async def show_invoices(message: types.Message):
    await bot.send_invoice(message.from_user.id, **NoteBook.generate_invoice(), payload='123456')


@dp.shipping_query_handler
async def choice_shipping(query: types.ShippingQuery):
    # проверим адрес доставки
    if query.shipping_address.country_code == 'RU':
        # вернем варианты доставки
        await bot.answer_shipping_query(shipping_options=[
            POST_REGULAR_SHIPPING,
            POST_FAST_SHIPPING,
            PICKUP_SHIPPING
        ], shipping_query_id=query.id, ok=True)
    elif query.shipping_address.country_code == 'US':
        # вернем варианты доставки (нет)
        await bot.answer_shipping_query(shipping_query_id=query.id, ok=False,
                                        error_message='Доставки в данный регион нет')
    else:
        # вернем варианты доставки( только почта)
        await bot.answer_shipping_query(shipping_options=[
            POST_REGULAR_SHIPPING,
        ], shipping_query_id=query.id, ok=True)


@dp.pre_checkout_query_handler()
async def process_pre_checkout(query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=query.id, ok=True)
    await bot.send_message(chat_id=query.from_user.id, text='Спасибо за покупку')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
