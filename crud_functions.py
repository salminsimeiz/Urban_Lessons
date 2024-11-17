import sqlite3
import logging


logging.basicConfig(level=logging.INFO, filename="products_db.log", encoding="UTF-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")


def initiate_db():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    cursor.execute('''
       CREATE TABLE IF NOT EXISTS Products(
       id INTEGER PRIMARY KEY,
       title TEXT UNIQUE NOT NULL,
       description TEXT,
       price INTEGER NOT NULL
       );
       ''')
    connection.commit()
    connection.close()

    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute('''
       CREATE TABLE IF NOT EXISTS Users(
       id INTEGER PRIMARY KEY,
       username TEXT NOT NULL,
       email TEXT NOT NULL,
       age INTEGER NOT NULL,
       balance INTEGER NOT NULL
       );
       ''')
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    all_products = cursor.fetchall()
    connection.commit()
    return all_products


def add_user(username, email, age):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (username, email, age, 1000))
    logging.info("go")
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    res = cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    if res.fetchone() is None:
        return False
    else:
        return True


if __name__ == "__main__":
    initiate_db()
    """try:
        for i in range(1, 5):
            cursor.execute("INSERT OR IGNORE  INTO Products(title, description, price)  VALUES(?, ?, ?)",
                           (f"Product{i}", f"Описание{i}", f"{i * 100}"))
    except sqlite3.DatabaseError as err:
        print("Error:", err)
    else:
        connection.commit()
    add_user("vera", "qw@err.io", 56)
    print(is_included("vera"))"""
