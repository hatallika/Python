# Обработка сообщений
# Машина состояний
import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import CommandStart, Command

# Хранение состояний
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

load_dotenv()
TOKEN = os.getenv('TOKEN')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN, parse_mode='html')  # Форматирование текста в HTML

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Класс состояний, 3 для примера
class Test(StatesGroup):
    Q1 = State()
    Q2 = State()
    Q3 = State()


@dp.message_handler(Command('test'))
async def start_test(message: types.Message):
    await message.answer('Вы начали тестирование.\n'
                         '<b>Вопрос №1</b>\n\n'
                         'Что выведет код?:\n <i>print(set([1, 2, 3, 1]))</i>')
    # await Test.first()  # Переключи на первое состояние
    await Test.Q1.set()


# Обработка состояния
@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)

    # # Варианты обновления стейта
    # await state.update_data(
    #     {
    #     'answer1': answer
    #     }
    # )
    # async with state.proxy() as data:
    #     data['answer1'] = answer
    await message.answer('<b>Вопрос №2</b>\n\n'
                         '<i>Какая функция называется анонимной?</i>')
    # await Test.Q2.set()
    await Test.next()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    # data = await state.get_data()
    # answer1 = data.get('answer1')
    answer2 = message.text
    await state.update_data(answer2=answer2)
    await message.answer('<b>Вопрос №3</b>\n\n'
                         '<i>Что такое list?</i>')
    await Test.next()


@dp.message_handler(state=Test.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    # Получим данные из стейта
    data = await state.get_data()
    answer1 = data.get('answer1')
    answer2 = data.get('answer2')
    answer3 = message.text

    await message.answer('Спасибо за ваши ответы')
    await message.answer(f'Ответ на первый вопрос: {answer1}')
    await message.answer(f'Ответ на второй вопрос: {answer2}')
    await message.answer(f'Ответ на третий вопрос: {answer3}')

    await state.finish()
    # await state.reset_state(with_data=False)
    # await state.reset_data()


@dp.message_handler(state='enter_email')
async def answer_q4(message: types.Message, state: FSMContext):
    answer = state.get_data()
    # Можем отправить answer, допустим, на почту
    await state.reset_state()


@dp.message_handler()
async def answer_q5(message: types.Message, state: FSMContext):
    # await message.answer()
    await state.set_state('enter_email')
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
