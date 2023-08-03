# Домшнее задание Обработка сообщения в чат-боте:#
# Реализация обработки сообщений в чат боте
#
# Планируемый результат:#
# Изучение вариантов обработки сообщений

# Напишем программу тестирование с вариантами ответов
import os
import logging
import re

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import CommandStart, Text

# Хранение состояний
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

load_dotenv()
TOKEN = os.getenv('TOKEN')
logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)


class MyStates(StatesGroup):
    Step1 = State()
    Step2 = State()
    Step3 = State()


victorina = [
    {
        'id': 1,
        'question': 'Как называется еврейский Новый год?',
        'answers': ['Ханука', 'Йом Кипур', 'Кванза', 'Рош ха-Шана'],
        'correct': 'Ханука',
    },
    {
        'id': 2,
        'question': 'Кто из этих персонажей не дружит с Гарри Поттером?',
        'answers': ['Рон Уизли', 'Невилл Лонгботтом', 'Драко Малфой', 'Гермиона Грейнджер'],
        'correct': 'Драко Малфой',
    },
    {
        'id': 3,
        'question': 'Какое животное не фигурирует в китайском зодиаке?',
        'answers': ['Дракон', 'Кролик', 'Собака', 'Колибри'],
        'correct': 'Колибри',
    },

]

step = 0
score = 0


def get_keyboard(num, answers_list: list):
    buttons = []
    for i in range(len(answers_list)):
        buttons.append(types.InlineKeyboardButton(text=answers_list[i], callback_data=f'question_{num}_{i}'))

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


# @dp.message_handler(CommandStart(deep_link=re.compile(r'^[0-9]{4,15}$')))
@dp.message_handler(CommandStart())
async def start_bot(message: types.Message):
    await message.answer('Добро пожаловать в игру!')
    await message.answer('Выберите вариант ответа\n'
                         f'Вопрос: {victorina[step]["question"]}',
                         reply_markup=get_keyboard(step, victorina[step]['answers']))


# Получаем ответ от пользователя с клавиатуры
@dp.callback_query_handler(Text(startswith='question'))
async def callback_answer(call: types.CallbackQuery, state: FSMContext):
    global step
    global score
    data = call.data.split('_')
    question = int(data[1])
    answer = int(data[2])

    # await call.message.answer(f'Был вопрос: {victorina[question]["question"]}\n'
    #                           f'Ваш ответ: {victorina[question]["answers"][answer]}')

    # Проверка
    if victorina[question]["correct"] == victorina[question]["answers"][answer]:
        score += 1
        await call.message.answer(f'Это правильный ответ, ваш счет: {score}')
    else:
        await call.message.answer(f'Ответ не верный, ваш счет: {score}')

    await call.answer()

    # переход к слеюующим вопросам (без стейта так как переход по нажатию с клавиатуры)
    step += 1
    if step < len(victorina):
        await call.message.answer('Выберите вариант ответа\n'
                                  f'Вопрос: {victorina[step]["question"]}',
                                  reply_markup=get_keyboard(step, victorina[step]['answers']))
    else:
        await call.message.answer(f'Игра закончилась, ваш счет: {score}')
        score = 0
        step = 0


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
