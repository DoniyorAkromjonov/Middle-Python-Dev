# Создать класс
class Car:
    pass

#Конструктор класса
class Car1:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

class Car12:
    def __init__(self, brand, year, hp):
        self.brand = brand
        self.year = year
        self.hp= hp

# Создаём обьект и вводим инфу в обьект(создаём машину)
my_car1 = Car1("Toyota", 2020)
my_car2 = Car1("Chevrolet", 2018)
my_car3 = Car12("Rols Roys", 2022, 500)

# Выводим инфу про машин
print(my_car1.brand)
print(my_car1.year)

print(my_car2.brand)
print(my_car2.year)

print(my_car3.brand)
print(my_car3.year)
print(my_car3.hp)
