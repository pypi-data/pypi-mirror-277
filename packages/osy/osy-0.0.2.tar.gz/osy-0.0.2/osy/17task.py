"""
18. Написать программу с интерактивным консольным меню (т.е. вывод списка действий по цифрам) по вычислению площади прямоугольника (родительский класс), и периметра прямоугольника (дочерний класс) по задаваемой с клавиатуры длине сторон прямоугольника. Содержание меню: 1. Вычислить площадь прямоугольника. 2. Вычислить периметр прямоугольника. (20 баллов)
"""


import datetime

class Automobile:
    def __init__(self, brand, power, seats):
        self.brand = brand
        self.power = power
        self.seats = seats

    def calculate_quality(self):
        return 0.1 * self.power * self.seats

    def display_info(self):
        print("Brand:", self.brand)
        print("Power (kW):", self.power)
        print("Number of Seats:", self.seats)
        print("Quality (Q):", self.calculate_quality())


class Car(Automobile):
    def __init__(self, brand, power, seats, year):
        super().__init__(brand, power, seats)
        self.year = year

    def calculate_quality(self):
        current_year = datetime.datetime.now().year
        base_quality = super().calculate_quality()
        return base_quality - 1.5 * (current_year - self.year)

    def display_info(self):
        super().display_info()
        print("Year of Manufacture:", self.year)
        print("Quality (Qp):", self.calculate_quality())


# Пример использования классов
car1 = Car("Toyota", 120, 5, 2015)
print("Car 1:")
car1.display_info()
print()

car2 = Car("BMW", 200, 4, 2018)
print("Car 2:")
car2.display_info()