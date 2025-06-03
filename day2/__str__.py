# __str__ помогает вывести ответ приятно для пользователя

class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User: {self.name}"

u = User("Alice")
x = User("Alex")
print(u)  # 👉 User: Alice
print(x)
