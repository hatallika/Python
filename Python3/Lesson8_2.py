# Семинар 3_8_2 Ограничение доступа
# Система платежей (Qiwi)
import datetime
import logging
import os
import uuid
import pyqiwi
from dataclasses import dataclass

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.markdown import hlink, hcode

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('aiogram').setLevel(logging.INFO)

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())


# @dp.message_handler()
# async def start_bot(message: types.Message):
#     await message.answer('hello')

@dataclass
class Item:
    id: int
    title: str
    description: str
    price: int
    photo_link: str


Notebook = Item(
    id=1,
    title='Ноутбук Lenovo IP Gaming 3',
    description='Ноутбук Lenovo IdeaPad Gaming 3 15IMH05 включает в себя 15.6-дюймовый экран, основу которого составила'
                ' матрица IPS, позволяющая вам насладиться невероятной четкостью и детализацией каждой картинки.',
    price=1,
    photo_link='https://c.dns-shop.ru/thumb/st4/fit/500/500/ca59f0087d33d5cbbf8d7a93ce157c74/63add0435dc2ca1f4082d79c725ff635bf24115760a1825efa496a176cf2d807.jpg',
)

Notebook2 = Item(
    id=2,
    title='Ноутбук Lenovo IP Gaming 3',
    description='Ноутбук Lenovo IdeaPad Gaming 3 15IMH05 включает в себя 15.6-дюймовый экран, основу которого составила'
                ' матрица IPS, позволяющая вам насладиться невероятной четкостью и детализацией каждой картинки.',
    price=2,
    photo_link='https://c.dns-shop.ru/thumb/st4/fit/500/500/ca59f0087d33d5cbbf8d7a93ce157c74/63add0435dc2ca1f4082d79c725ff635bf24115760a1825efa496a176cf2d807.jpg',
)

items = [Notebook, Notebook2]


class NotEnoughMoney(Exception):
    pass


class NotPaymentFound(Exception):
    pass


# wallet = pyqiwi.Wallet(token=os.getenv('QIWI_TOKEN'), number=os.getenv('QIWI'))


# класс платежа
@dataclass
class Payment:
    amount: int
    id: str = None

    # Создать id
    def create(self):
        self.id = str(uuid.uuid4())

    # Проверка
    def check_payment(self):
        # start_date = datetime.datetime.now() - datetime.timedelta(days=2)
        # # transactions = wallet.history(start_date=start_date).get('transactions')
        # for transaction in transactions:
        #     if transaction.comment:
        #         # если есть id пользователя, сделавшего платеж
        #         if str(self.id) in transactions.comment:
        #             # проверка средств
        #             if float(transaction.total.amount) >= float(self.amount):
        #                 return True
        #             else:
        #                 return False
        #         else:
        #             raise NotPaymentFound
        pass

    @property
    def invoice(self):
        # ссылка на оплату
        link = 'https://oplata.qiwi...'
        # передаем в коментарий id
        return link.format(publicKey=os.getenv('QIWI_PUB'), amount=self.amount, comment=self.id)


def b_keyboard(item_id):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Купить', callback_data=f'buy: {item_id}')
            ]
        ]
    )
    return keyboard


paid_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Оплатил', callback_data='paid')
        ],
        [
            InlineKeyboardButton(text='Отмена', callback_data='cancel')
        ]
    ]
)


@dp.callback_query_handler(text_contains='buy')
async def create_invoice(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    # parsing callback_data
    item_id = call.data.split(':')[-1]
    item_id = int(item_id) - 1
    item = items[item_id]
    amount = item.price

    payment = Payment(amount=amount)
    payment.create()

    await call.message.answer(
        '\n'.join([
            f'Оплатите не менее  {amount:.2f} по номеру или по адресу',
            '',
            hlink(os.getenv('QIWI'), url=payment.invoice),
            'и обязательно укажите ID платежа',
            hcode(payment.id)
        ]),
        reply_markup=paid_keyboard
    )
    await state.set_state('qiwi')
    await state.update_data(payment=payment)


@dp.callback_query_handler(text='cancel', state='qiwi')
async def cancel_payment(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text('Отменено')
    await state.finish()


@dp.message_handler(text='paid', state='qiwi')
async def approve_payment(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    payment: Payment = data.get('payment')
    try:
        payment.check_payment()
    except NotPaymentFound:
        await call.message.answer('Транзакция не найдена')
        return
    except NotEnoughMoney:
        await call.message.answer('Недостаточная сумма на кошельке')
        return
    else:
        await call.message.answer('Успешная оплата')
        await call.message.delete_reply_markup()
        await state.finish()


@dp.message_handler(Command('items'))
async def show_items(message: types.Message):
    caption = """
        Название продукта: {title}
        <i>Описание</i>:
        {description}
        
        <u>Цена: </u> {price:.2f}<b>RUB</b>
    """
    for item in items:
        await message.answer_photo(
            photo=item.photo_link,
            caption=caption.format(
                title=item.title,
                description=item.description,
                price=item.price
            ), reply_markup=b_keyboard(item_id=item.id)
        )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
