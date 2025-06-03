# __repr__ выводит ответ удобно для копирования и на консоли

class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"User('{self.name}')"

u = User("Alice")
print(repr(u))  # 👉 User('Alice')
