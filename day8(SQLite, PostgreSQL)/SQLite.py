import sqlite3

# Подключение к базе данных (создаст файл, если не существует)
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# CREATE: создаём таблицу
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")

# INSERT
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))
conn.commit()

# SELECT
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall() # берёт всю инфу из users и созраняет в еременную rows
print("Users:", rows)

# UPDATE
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (26, "Alice"))
conn.commit()

# DELETE
cursor.execute("DELETE FROM users WHERE name = ?", ("Bob",))
conn.commit()

# Проверка
cursor.execute("SELECT * FROM users")
print("After changes:", cursor.fetchall())

conn.close()
