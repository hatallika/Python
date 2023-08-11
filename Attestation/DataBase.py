import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        # открываем соединение
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(result))

    def add_user(self, user_id, username, fullname, phone):
        with self.connection:
            return self.cursor.execute("INSERT INTO users (user_id, username, fullname, phone) VALUES (?, ?, ?, ?)",
                                       (user_id, username, fullname, phone))

    def get_users_id(self):
        with self.connection:
            return self.cursor.execute('SELECT user_id, username FROM users').fetchall()

    def create_table(self):
        with self.connection:
            return self.cursor.execute("""
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,                    
                    username TEXT,
                    fullname TEXT,
                    phone TEXT                    
                );
            """)
