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

    def get_products(self, category=None):
        if category:
            with self.connection:
                return self.cursor.execute(
                    'SELECT id, title, category, description, price, discount, img_url FROM products WHERE category=?',
                    (category,)).fetchall()
        else:
            with self.connection:
                return self.cursor.execute('SELECT title, description, price FROM products').fetchall()

    def get_categories(self):
        with self.connection:
            return self.cursor.execute("SELECT DISTINCT category FROM products WHERE id > 0").fetchall()

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

    def create_table_products(self):
        with self.connection:
            return self.cursor.execute("""
                CREATE TABLE products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    category TEXT,
                    description TEXT,
                    price INTEGER,
                    discount INTEGER,
                    img_url TEXT           
                );
            """)

    def add_product(self, title, category, description, price, discount, img_url):
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO products (title, category, description,"
                "price, discount, img_url) VALUES (?, ?, ?, ?, ?, ?)",
                (title, category, description, price, discount, img_url))
