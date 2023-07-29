# Настройка webhook для чат ботов
# Работа с базой данных SQLite БД
import sqlite3

conn = sqlite3.connect('test.db')
# conn = sqlite3.connect(':memory:')
cur = conn.cursor()
# cur.execute("""CREATE TABLE users(name text, last_name text, city text)""")
# cur.execute("""INSERT INTO users VALUES('Иван', 'Иванов', 'Москва')""")
users = [
    ('Сергей', 'Петров', 'Санкт-Петербург'),
    ('Андрей', 'Сергеев', 'Ижевск'),
    ('Василий', 'Андреев', 'Краснодар'),
]

# Множественный запрос
# cur.executemany("INSERT INTO users VALUES(?, ?, ?)", users)
# sql = 'SELECT * FROM users'
# cur.execute(sql)
# print(cur.fetchall())
# user_list = cur.fetchall()
# for user in user_list:
#     print(user)


# user_list = cur.fetchone()
# print(user_list)

# user_list = cur.fetchmany(3)
# print(user_list)

# sql = 'SELECT * FROM users WHERE name=?'
# cur.execute(sql, ['Иван'])
# print(cur.fetchall())

# Сортировка
# for row in cur.execute('SELECT name FROM users ORDER BY city'):
#     print(row)

# for row in cur.execute('SELECT rowid, * FROM users ORDER BY name'):
#     print(row)

# Изменение данных
# sql = "UPDATE users SET city='Казань' WHERE name='Иван'"
# cur.execute(sql)
# cur.execute("SELECT * FROM users")
# for item in cur.fetchall():
#     print(item)

# sql = "UPDATE users SET city=? WHERE name=?"
# cur.execute(sql, ['Москва', 'Андрей'])
# cur.execute("SELECT * FROM users")
# for item in cur.fetchall():
#     print(item)

# Удаление данных
sql = "DELETE FROM users WHERE name='Иван'"
cur.execute(sql)
cur.execute("SELECT * FROM users")
for item in cur.fetchall():
    print(item)
    
cur.close()
conn.commit()
conn.close()
