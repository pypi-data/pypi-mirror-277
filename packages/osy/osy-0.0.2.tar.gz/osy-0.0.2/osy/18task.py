"""
Написать программу с интерактивным консольным меню (т.е. вывод списка действий по цифрам) по вычислению площади прямоугольника (родительский класс), и периметра прямоугольника (дочерний класс) по задаваемой с клавиатуры длине сторон прямоугольника. Содержание меню: 1. Вычислить площадь прямоугольника. 2. Вычислить периметр прямоугольника. (20 баллов)
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


class RectangleMenu:
    def __init__(self):
        self.rectangle = None

    def display_menu(self):
        print("1. Вычислить площадь прямоугольника.")
        print("2. Вычислить периметр прямоугольника.")
        print("3. Выйти из программы.")

    def create_rectangle(self):
        length = float(input("Введите длину прямоугольника: "))
        width = float(input("Введите ширину прямоугольника: "))
        self.rectangle = Rectangle(length, width)

    def run_menu(self):
        while True:
            self.display_menu()
            choice = input("Выберите действие (1/2/3): ")

            if choice == '1':
                if not self.rectangle:
                    self.create_rectangle()
                area = self.rectangle.calculate_area()
                print(f"Площадь прямоугольника: {area}")
            elif choice == '2':
                if not self.rectangle:
                    self.create_rectangle()
                perimeter = self.rectangle.calculate_perimeter()
                print(f"Периметр прямоугольника: {perimeter}")
            elif choice == '3':
                print("Программа завершена.")
                break
            else:
                print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")


menu = RectangleMenu()
menu.run_menu()
