import sqlite3
import logging


logging.basicConfig(level=logging.INFO, filename="products_db.log", encoding="UTF-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")

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
logging.info("wet")


def initiate_db():
    try:
        for i in range(1, 5):
            cursor.execute("INSERT INTO Products(title, description, price)  VALUES(?, ?, ?)",
                           (f"Product{i}", f"Описание{i}", f"{i * 100}"))
    except sqlite3.DatabaseError as err:
        print("Error:", err)
    else:
        connection.commit()


def get_all_products():
    cursor.execute("SELECT * FROM Products")
    all_products = cursor.fetchall()
    connection.commit()
    return all_products


if __name__ == "__main__":
    initiate_db()
    connection.commit()
    connection.close()
