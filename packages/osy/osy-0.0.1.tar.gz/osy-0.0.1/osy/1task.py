import os
import math
"""1. Написать программу с интерактивным консольным меню (т.е. вывод 
списка действий по цифрам) по вычислению площади круга (родительский класс), 
длины окружности (подкласс) и объема шара (подкласс) по задаваемому с 
клавиатуры радиусу. Содержание меню: 1. Вычислить площадь круга. 2. 
Вычислить длину окружности. 3. Вычислить объем шара. (20 баллов)"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        print(math.pi * self.radius ** 2)

class Circumference(Circle):
    def calculate_circumference(self):
        print(2 * math.pi * self.radius)

class Sphere(Circle):
    def calculate_volume(self):
        print((4 / 3) * math.pi * self.radius ** 3)

def menu(entercom: str, *func):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(entercom)
    command = input('Команда: ')
    if command.isdigit() and len(func) > int(command) - 1 >= 0:
        func[int(command) - 1]()
    elif command.isdigit() and int(command) == len(func) + 1:
        return False
    else:
        print('Такой команды нет...')
    input('\nEnter для продолжения\n')
    return True

def main():
    radius = float(input("Введите радиус: "))
    circle = Circle(radius)
    circumference = Circumference(radius)
    sphere = Sphere(radius)
    run = True
    commands = """==========================================================================
    1. Вычислить площадь круга. 
    2. Вычислить длину окружности. 
    3. Вычислить объем шара.
    4. Завершить"""

    while run:
        run = menu(commands, circle.calculate_area, circumference.calculate_circumference, sphere.calculate_volume)

if __name__ == '__main__':
    main()
