"""
С помощью функции reduce() вычислить двойной факториал заданного натурального числа n (для четного или нечетного n). (20 баллов)
"""
from functools import reduce

def double_factorial(n):
    if n <= 0:
        return 1
    # Генерируем список чисел от n до 1 с шагом 2
    numbers = range(n, 0, -2)
    # Используем функцию reduce() для перемножения всех чисел
    result = reduce(lambda x, y: x * y, numbers)
    return result

n = 7  # заданное натуральное число
double_fact = double_factorial(n)
print(f"Двойной факториал числа {n} равен {double_fact}")