import sqlite3

# Подключение к базе данных (файл создастся автоматически)
conn = sqlite3.connect("my_database.db")

# Создаём курсор
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# Добавление данных
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))

# Сохраняем изменения
conn.commit()

# Чтение данных
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Закрытие соединения
conn.close()
