# __eq__ сравнивает ифромации как люди сравнимвают и если они совпадают выводит True, если нет то False


class User:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

u1 = User("Alice")
u2 = User("Alice")
print(u1 == u2)  # 👉 True


# 2 пример

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

p1 = Product("iPhone 15", 999)
p2 = Product("iPhone 15", 999)
p3 = Product("iPhone 15", 899)

print(p1 == p2)  # 👉 True (одинаковое имя и цена)
print(p1 == p3)  # 👉 False (разная цена)


