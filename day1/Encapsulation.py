class BankAccount:
    def __init__(self):
        self.__balance = 0  # скрытая переменная

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    # геттер чтоб выводить инфу безопасно
    def get_balance(self):
        return self.__balance
# выводим инфу
acc = BankAccount()
acc.deposit(100)
print(acc.get_balance())


# 2 Пример
class User:
    def __init__(self, name):
        self.__name = name


    def set_name(self, new_name):  # сеттер чтоб менять значение
        if isinstance(new_name, str) and new_name != "":
            self.__name = new_name


    def get_name(self): # геттер чтоб выводить безопасно инфу
        return self.__name

user = User("Alice")
user.set_name("Shalala")  # безопасное обновление
print(user.get_name())  # new nam
