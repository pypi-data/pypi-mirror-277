""""11. Создайте класс Speed (Скорость), имеющий атрибуты: value (значение),
unit (единица измерения). При изменении единицы измерения значение должно
соответственно меняться. Например, при переходе от км/ч к м/с и наоборот.
Например, 20 км/ч = 5.56 м/с. Допустимые значения свойства unit: ‘м/с’, ‘км/ч’.
Организуйте эту проверку. Продемонстрируйте работу с классом. (20 баллов)"""
class Speed:
    def __init__(self, value, unit):
        self.value = value
        if unit == 'км/ч' or unit == 'м/с':
            self.unit = unit
        else:
            self.unit = None

    def change_unit(self):
        if self.unit != None:
            new_unit = str(input('Введите новую единицу измерения: '))
            if new_unit == self.unit:
                print(f"Единицы измерения не поменялись. Значение: {self.value} {self.unit}")
            elif new_unit == 'км/ч':
                self.value = (self.value * 3600) / 1000
                self.unit = 'км/ч'
                print(f"Измененное значение: {round(self.value,2)} {self.unit}")
            elif new_unit == 'м/с':
                self.value = (self.value * 1000) / 3600
                self.unit = 'м/с'
                print(f"Измененное значение: {round(self.value,2)} {self.unit}")
            else:
                print("Вы ввели недопустимую единицу измерения")
        else:
            print("Вы ввели недопустимую единицу измерения")

# Пример использования класса
a = Speed(20, 'м/ч')
print(a.value, a.unit)
a.change_unit()