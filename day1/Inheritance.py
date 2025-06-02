class Vehicle:
    def drive(self):
        print("Driving...")

class Car2(Vehicle):
    def honk(self, brand):
        print("Beep!")
        self.brand = brand


# Создаём обьект
my_car = Car2()
# выводим инфу про машин
my_car.drive()  # Driving...
my_car.honk("bmw") # Beep!

print(my_car.brand)
