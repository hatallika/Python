from dataclasses import dataclass
from aiogram.types import LabeledPrice
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()
PAYMENT_TOKEN = os.getenv('PAYMENT_TOKEN')


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


def get_product_class_item(product: dict, id_):
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
        start_parameter='create_invoice_'+id_,
        photo_url=product['img_url'],
        photo_size=600,
        need_shipping_address=True,
        is_flexible=True
    )
