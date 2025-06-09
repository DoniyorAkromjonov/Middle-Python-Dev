import psycopg2

# Подключение к PostgreSQL
conn = psycopg2.connect(
    dbname="posgresql_db",
    user="username",
    password="your_passowrd",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# CREATE
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER
)
""")
conn.commit()

# INSERT
cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Alice", 25))
cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Bob", 30))
conn.commit()

# SELECT
cursor.execute("SELECT * FROM users")
print("Users:", cursor.fetchall())

# UPDATE
cursor.execute("UPDATE users SET age = %s WHERE name = %s", (26, "Alice"))
conn.commit()

# DELETE
cursor.execute("DELETE FROM users WHERE name = %s", ("Bob",))
conn.commit()

# Проверка
cursor.execute("SELECT * FROM users")
print("After changes:", cursor.fetchall())

conn.close()
