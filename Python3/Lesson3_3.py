import os
import logging
import sqlite3
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import CommandStart

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Логирование
logging.basicConfig(level=logging.INFO)


# Создадим базу данных (обычно в отдельном файле)
class Database:
    def __init__(self, path_to_db='test1.db '):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql, parameters: tuple = None, fetchone=False, fetchall=False, fetchmany=False, commit=False):
        if not parameters:
            parameters = tuple()  # Пустой кортеж
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        # if fetchmany:
        #     data = cursor.fetchmany(fetchmany)
        connection.close()
        return data

    def create_table(self, name):
        sql = f"""
                CREATE TABLE {name}(
                id int NOT NULL, 
                name varchar(255) NOT NULL,
                email varchar(255),
                PRIMARY KEY(id)
                );
                """
        return self.execute(sql)

    def add_user(self, id: int, name: str, email: str = None):
        sql = "INSERT INTO users(id, name, email) VALUES (?, ?, ?)"
        parameters = (id, name, email)
        self.execute(sql, parameters=parameters, commit=True)

    @staticmethod
    def format_args(sql, paramerters: dict):
        sql += " AND ".join([f'{item} = ?' for item in paramerters])
        return sql, tuple(paramerters.values())

    def select_all_users(self):
        sql = "SELECT * FROM users"
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM users"
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)

    def count_users(self):
        return self.execute('SELECT COUNT(*) FROM users', fetchone=True)

    def update_email(self, email, id):
        sql = "UPDATE users SET email=? WHERE id=?"
        self.execute(sql, parameters=(email, id), commit=True)

    def delete_all_user(self):
        self.execute('DELETE FROM users WHERE TRUE', commit=True)


def logger(statement):
    print(f"""
__________________________________
EXECUTING
{statement}
__________________________________    
    """)


db = Database()
try:
    db.create_table('users')
    print('Таблица создана')
except Exception as err:
    print(err)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        print(err)
    count_users = db.count_users()[0]
    await message.answer(
            '\n'.join([
                f'Привет, {message.from_user.full_name}!',
                f'Ты был занесен в базу данных ',
                f'В базе данных {count_users} пользователей'
            ])
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
