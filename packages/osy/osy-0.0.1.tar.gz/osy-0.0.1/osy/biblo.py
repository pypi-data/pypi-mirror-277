# AlgorithmsExamSummer/__init__.py

# Пустой файл __init__.py
# Этот файл нужен для того, чтобы Python распознал папку AlgorithmsExamSummer как пакет
def consol_menu():
    """
    Документация для задания 1.
    1. Написать программу с интерактивным консольным меню
    """

    """
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
    commands = """"""

    while run:
        run = menu(commands, circle.calculate_area, circumference.calculate_circumference, sphere.calculate_volume)

if __name__ == '__main__':
    main()
"""

def stack():
    """
    Документация для задания 2.
    Создать стек.
    """
""""
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def swap_first_and_last(self):
        if len(self.items) < 2:
            return

        first_element = self.items[0]
        self.items[0] = self.items[-1]
        self.items[-1] = first_element


# Пример использования
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Стек до замены:")
print(stack.items)

stack.swap_first_and_last()

print("\nСтек после замены:")
print(stack.items)"""

def pos_neg():
    """Фильтр полож и отриц числа
    """
"""
def is_positive(num):
    return num > 0

def is_negative(num):
    return num < 0

positive_list = list(filter(is_positive, A))
negative_list = list(filter(is_negative, A))"""

def plane():
    """
        Документация для задания 2.
        Создать стек.
    """

""""class Plane:
    def __init__(self, name, passengers, route):
        self.name = name
        self.passengers = passengers
        self.route = route

    @staticmethod
    def calculate_load(passengers):
        max_capacity = 200
        load_percentage = (passengers / max_capacity) * 100
        return load_percentage

    @staticmethod
    def same_route_planes(planes, route):
        same_route_planes = [plane.name for plane in planes if plane.route == route]
        return same_route_planes

    @staticmethod
    def average_load(planes):
        total_passengers = sum(plane.passengers for plane in planes)
        average_load = total_passengers / len(planes)
        return average_load

# Пример использования
plane1 = Plane("Boeing 747", 180, "New York - London")
plane2 = Plane("Airbus A380", 210, "Paris - Tokyo")
plane3 = Plane("Boeing 737", 150, "London - Dubai")

planes = [plane1, plane2, plane3]

print(f"Загрузка самолета {plane1.name}: {Plane.calculate_load(plane1.passengers)}%")
print(f"Самолеты, летящие по маршруту 'New York - London': {Plane.same_route_planes(planes, 'New York - London')}")
print(f"Средняя загрузка всех самолетов: {Plane.average_load(planes)} пассажиров")"""

def mapfilreduce():
    """Пример map filter reduce алгоритма"""

"""
from functools import reduce

# Предложение без знаков препинания
sentence = "Дано предложение без знаков препинания"

# Разделение предложения на список слов
words = sentence.split()

# Отброс последней буквы у каждого слова и объединение слов длиной более 5 символов
result = reduce(lambda x, y: x + y, map(lambda word: word[:-1], filter(lambda word: len(word) > 5, words)))

print(result)
"""

def decorator():
    """Пример для заданий с декораторм"""
""""
def not_none(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result is None:
            raise ValueError("Функция вернула значение None")
        return result
    return wrapper

# Пример использования декоратора
@not_none
def example_function(value):
    if value:
        return value
    else:
        return None

try:
    print(example_function("Hello"))
    print(example_function(None))
except ValueError as e:
    print("Ошибка:", e)
#print(f"Тип возвращаемого значения: {type(result).__name__}")    
"""

def binary_add():
    """Сложение двоичных"""
""""
def binary_addition(bin1, bin2):
    if not bin1:
        return bin2
    if not bin2:
        return bin1

    if bin1[-1] == '1' and bin2[-1] == '1':
        return binary_addition(binary_addition(bin1[:-1], '1') + '0', bin2[:-1])
    elif bin1[-1] == '0' and bin2[-1] == '0':
        return binary_addition(bin1[:-1], bin2[:-1]) + '0'
    else:
        return binary_addition(bin1[:-1], bin2[:-1]) + '1'

# Пример использования
bin_num1 = '1010'  # Положительное число в двоичной системе
bin_num2 = '1101'  # Отрицательное число в двоичной системе

result = binary_addition(bin_num1, bin_num2)
print(f"Сумма чисел {bin_num1} и {bin_num2} в двоичной системе: {result}")
"""

def merge_sort():
    """Сортировка слиянием"""

"""
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def sort_repair_counts(arr):
    merge_sort(arr)
    return arr

# Пример списка количества предыдущих ремонтов машин "Жигули"
repair_counts = [3, 1, 5, 2, 4]

sorted_repair_counts = sort_repair_counts(repair_counts)
print("Отсортированное количество предыдущих ремонтов машин 'Жигули' по убыванию:")
print(sorted_repair_counts)
"""

def od_linked_list():
    """31. Реализовать однонаправленный связанный список (реализовать класс для
элементов списка). Преобразовать строку 'Eeny, meeny, miney, moe; Catch a tiger by
his toe.' в связный список символов строки и удалить из него все элементы
содержащие гласные буквы. (20 баллов)"""
""""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

def remove_vowels_from_linked_list(linked_list):
    vowels = "aeiouAEIOU"
    current = linked_list.head
    prev = None

    while current:
        if current.data in vowels:
            if prev is None:
                linked_list.head = current.next
            else:
                prev.next = current.next
        else:
            prev = current
        current = current.next

# Создаем связанный список из строки
string = 'Eeny, meeny, miney, moe; Catch a tiger by his toe.'
char_list = LinkedList()
for char in string:
    char_list.append(char)

# Удаляем гласные буквы из связанного списка
remove_vowels_from_linked_list(char_list)
# Выводим итоговый связанный список
char_list.display()
"""
def factorial():
    """Вычесление двойного и обычного факториала"""

"""
def Fact(N):
    if N == 0:
        return 1
    else:
        return N * Fact(N - 1)

def Fact2(N):
    if N <= 0:
        return 1
    elif N == 1:
        return 1
    else:
        return N * Fact2(N - 2)

# Пример вызова функций для вычисления факториала и двойного факториала
N = 5
factorial_N = Fact(N)
double_factorial_N = Fact2(N)

print(f"Факториал {N}! = {factorial_N}")
print(f"Двойной факториал {N}!! = {double_factorial_N}")"""

def fruits():
    """Иерархия фруктов"""
"""
class Fruit:
    def __init__(self, name, price):
        self._name = name  # Защищенный атрибут
        self._price = price  # Защищенный атрибут
        self.quantity = 0  # Обычный атрибут

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

class Apple(Fruit):
    def __init__(self, name, price, color):
        super().__init__(name, price)
        self.color = color

class Banana(Fruit):
    def __init__(self, name, price, length):
        super().__init__(name, price)
        self.length = length

class Orange(Fruit):
    def __init__(self, name, price, origin):
        super().__init__(name, price)
        self._origin = origin  # Защищенный атрибут

    def get_origin(self):
        return self._origin

# Создание объектов
apple = Apple("Apple", 2.5, "Red")
banana = Banana("Banana", 1.5, "Medium")
orange = Orange("Orange", 3.0, "Spain")

# Попытка изменить защищенный атрибут _name
apple._name = "Green Apple"
print(apple.get_name())  # Выведет "Apple"

# Попытка изменить защищенный атрибут _origin через метод
orange._origin = "Italy"
print(orange.get_origin())  # Выведет "Spain"

# Изменение обычного атрибута quantity
apple.quantity = 10
print(apple.quantity)  # Выведет 10
"""

def car_users_alf():
    """водители машин по алфавитк"""
"""
car_owners = {
    "Alice": "Toyota",
    "Bob": "Ford",
    "Charlie": "Chevrolet",
    "Eve": "BMW",
    "David": "Honda"

}

# Функция для сортировки выбором
def selection_sort(dictionary):
    keys = list(dictionary.keys())
    for i in range(len(keys)):
        min_index = i
        for j in range(i+1, len(keys)):
            if keys[j] < keys[min_index]:
                min_index = j
        keys[i], keys[min_index] = keys[min_index], keys[i]
    return keys

# Сортировка имен владельцев
sorted_names = selection_sort(car_owners)

# Вывод информации об автомобилях владельцев по алфавиту их имен
for name in sorted_names:
    print(f"{name}: {car_owners[name]}")
"""

def root():
    """Приближенное значение корня"""

"""
def f(x):
    # Здесь определите вашу функцию f(x)
    return x ** 2 - 4  # Пример: уравнение x^2 - 4 = 0


def Root(a, b, epsilon):
    if (b - a) < epsilon:
        return (a + b) / 2

    c = (a + b) / 2
    if f(a) * f(c) < 0:
        return Root(a, c, epsilon)
    else:
        return Root(c, b, epsilon)


# Заданный отрезок [a, b] и точность epsilon
a = 0
b = 3
epsilon = 0.0001

# Находим корень уравнения f(x) = 0 на отрезке [a, b] с заданной точностью
root = Root(a, b, epsilon)
print("Приближенное значение корня уравнения: ", root)
"""

def choose_sort():
    """СОРТИРОВКА ВЫБОРОМ"""
"""
def f(x):
    # Здесь определите вашу функцию f(x)
    return x ** 2 - 4  # Пример: уравнение x^2 - 4 = 0


def Root(a, b, epsilon):
    if (b - a) < epsilon:
        return (a + b) / 2

    c = (a + b) / 2
    if f(a) * f(c) < 0:
        return Root(a, c, epsilon)
    else:
        return Root(c, b, epsilon)


# Заданный отрезок [a, b] и точность epsilon
a = 0
b = 3
epsilon = 0.0001

# Находим корень уравнения f(x) = 0 на отрезке [a, b] с заданной точностью
root = Root(a, b, epsilon)
print("Приближенное значение корня уравнения: ", root)
"""

def land():
    """Создать класс Профиль местности, который хранит последовательность
высот, вычисленных через равные промежутки по горизонтали. Методы:
наибольшая высота, наименьшая высота, перепад высот (наибольший,
суммарный), крутизна (тангенс угла наклона; наибольшая, средняя), сравнение
двух профилей одинаковой длины (по перепаду, по крутизне)."""
"""
import math


class MapProfile:
    def __init__(self, list_h):
        self.heights = list_h

    def highest(self):
        return max(self.heights)

    def lowest(self):
        return min(self.heights)

    def max_drop(self):
        max_drop = 0
        for i in range(len(self.heights) - 1):
            for j in range(i + 1, len(self.heights)):
                drop = abs(self.heights[j] - self.heights[i])
                if drop > max_drop:
                    max_drop = drop
        return max_drop

    def total_drop(self):
        total = 0
        for i in range(len(self.heights) - 1):
            total += abs(self.heights[i] - self.heights[i + 1])
        return total

    def max_slope(self, horizontal_distance):
        max_slope = 0
        for i in range(len(self.heights) - 1):
            slope = abs(self.heights[i + 1] - self.heights[i]) / horizontal_distance
            if slope > max_slope:
                max_slope = slope
        return max_slope

    def average_slope(self, horizontal_distance):
        total_slope = 0
        for i in range(len(self.heights) - 1):
            total_slope += abs(self.heights[i + 1] - self.heights[i]) / horizontal_distance
        return total_slope / (len(self.heights) - 1)

    @staticmethod
    def compare_profiles(profile1, profile2, horizontal_distance):
        if len(profile1.heights) != len(profile2.heights):
            raise ValueError("Profiles must be of the same length")

        comparison = {
            "max_drop": profile1.max_drop() > profile2.max_drop(),
            "total_drop": profile1.total_drop() > profile2.total_drop(),
            "max_slope": profile1.max_slope(horizontal_distance) > profile2.max_slope(horizontal_distance),
            "average_slope": profile1.average_slope(horizontal_distance) > profile2.average_slope(horizontal_distance)
        }

        return comparison


# Пример использования:
profile1 = MapProfile([100, 200, 150, 300, 250])
profile2 = MapProfile([120, 180, 160, 280, 240])

print("Наибольшая высота профиля 1:", profile1.highest())
print("Наименьшая высота профиля 1:", profile1.lowest())
print("Наибольший перепад высот профиля 1:", profile1.max_drop())
print("Суммарный перепад высот профиля 1:", profile1.total_drop())
print("Наибольшая крутизна профиля 1:", profile1.max_slope(10))
print("Средняя крутизна профиля 1:", profile1.average_slope(10))

comparison = MapProfile.compare_profiles(profile1, profile2, 10)
print("Сравнение профилей (profile1 > profile2):", comparison)
"""

def binarytree():
    """Реализовать двоичное дерево в виде связанных объектов (реализовать
класс для элементов двоичного дерева) и реализовать симметричную процедуру
обхода двоичного дерева в виде рекурсивной функции. """
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def in_order_traversal(self):
        return self._in_order_recursive(self.root)

    def _in_order_recursive(self, node):
        result = []
        if node:
            result += self._in_order_recursive(node.left)
            result.append(node.value)
            result += self._in_order_recursive(node.right)
        return result

# Пример использования
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

print("In-order traversal:", tree.in_order_traversal())
"""

def ssd():
    """"""

"""
class Computer:
    def __init__(self, processor_name, clock_speed, ram):
        self.processor_name = processor_name
        self.clock_speed = clock_speed
        self.ram = ram

    def quality(self):
        return (0.1 * self.clock_speed) + self.ram

    def display_info(self):
        print(f"Processor Name: {self.processor_name}")
        print(f"Clock Speed (MHz): {self.clock_speed}")
        print(f"RAM (MB): {self.ram}")
        print(f"Quality (Q): {self.quality()}")

class AdvancedComputer(Computer):
    def __init__(self, processor_name, clock_speed, ram, ssd):
        super().__init__(processor_name, clock_speed, ram)
        self.ssd = ssd

    def quality(self):
        base_quality = super().quality()
        return base_quality + 0.5 * self.ssd

    def display_info(self):
        super().display_info()
        print(f"SSD (GB): {self.ssd}")
        print(f"Quality with SSD (Qp): {self.quality()}")

# Пример использования классов
if __name__ == "__main__":
    # Создание объекта базового класса
    computer = Computer("Intel i5", 3200, 8192)
    print("Basic Computer Info:")
    computer.display_info()

    print("\nAdvanced Computer Info:")
    # Создание объекта дочернего класса
    advanced_computer = AdvancedComputer("Intel i7", 3600, 16384, 512)
    advanced_computer.display_info()
"""

def dob_linked_list():
    """"""
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def insert_after_n(self, n, data):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        count = 0

        # Пройдем по списку до n-го элемента
        while current and count < n:
            current = current.next
            count += 1

        # Если текущий элемент не найден, значит n больше длины списка
        if current is None:
            print(f"Cannot insert after {n}-th element as the list has fewer elements.")
            return

        # Создаем новый узел
        new_node = Node(data)

        # Вставляем новый узел после текущего
        new_node.next = current.next
        new_node.prev = current

        if current.next:
            current.next.prev = new_node

        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Пример использования
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)

print("Initial list:")
dll.display()

n = 2  # Вставка после 2-го элемента (0-based index)
data_to_insert = 99

dll.insert_after_n(n, data_to_insert)

print(f"List after inserting {data_to_insert} after {n}-th element:")
dll.display()

"""

def circlied_linked_list():
    """"""
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display(self):
        nodes = []
        temp = self.head
        if self.head:
            while True:
                nodes.append(temp.data)
                temp = temp.next
                if temp == self.head:
                    break
        print(" -> ".join(nodes))

    def select_every_nth(self, n):
        selected = []
        if not self.head:
            return selected

        current = self.head
        prev = None

        while True:
            count = 1
            while count < n:
                prev = current
                current = current.next
                count += 1

            selected.append(current.data)
            prev.next = current.next  # Remove the selected node from the circle
            current = current.next  # Move to the next node

            if current == self.head:  # If we have completed a full circle, break
                break

        return selected


# Создание двух кольцевых списков с фамилиями шахматистов двух команд
team1 = CircularLinkedList()
team1.append("Player1_Team1")
team1.append("Player2_Team1")
team1.append("Player3_Team1")
team1.append("Player4_Team1")

team2 = CircularLinkedList()
team2.append("Player1_Team2")
team2.append("Player2_Team2")
team2.append("Player3_Team2")
team2.append("Player4_Team2")

print("Team 1:")
team1.display()

print("Team 2:")
team2.display()

# Ввод значений n и k
n = int(input("Enter the value of n for Team 1: "))
k = int(input("Enter the value of k for Team 2: "))

# Жеребьевка
selected_team1 = team1.select_every_nth(n)
selected_team2 = team2.select_every_nth(k)

print(f"Selected players from Team 1 (every {n}-th): {selected_team1}")
print(f"Selected players from Team 2 (every {k}-th): {selected_team2}")
"""

def tree_linked_list():
    """Вершины дерева вещественные числа. Описать функцию, которая
вычисляет среднее арифметическое всех вершин
дерева. Результат вывести в веб-интерфейс при помощи фреймворка Django. Базу
данных можно использовать по желанию, дизайн не обязателен: достаточно
обычных кнопок/списков."""

"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def calculate_average(node):
    if node is None:
        return (0, 0)  # Сумма и количество вершин

    left_sum, left_count = calculate_average(node.left)
    right_sum, right_count = calculate_average(node.right)

    total_sum = left_sum + right_sum + node.value
    total_count = left_count + right_count + 1

    return (total_sum, total_count)

# Пример использования функции
# Создаем дерево
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

total_sum, total_count = calculate_average(root)
average = total_sum / total_count

print("Среднее арифметическое всех вершин дерева:", average)
"""