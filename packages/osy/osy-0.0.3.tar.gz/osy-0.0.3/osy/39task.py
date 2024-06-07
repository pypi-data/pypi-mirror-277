import random

# Создание одномерного массива целых чисел размерности n
n = 20
array = [random.randint(-20, 20) for _ in range(n)]

# Вычисление сумм отрицательных и положительных элементов
sum_negative = sum([abs(num) for num in array if num < 0])
sum_positive = sum([num for num in array if num > 0])

# Сортировка массива в зависимости от условия
if sum_negative > sum_positive:
    # Сортировка по возрастанию
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
else:
    # Сортировка по убыванию
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if array[j] > array[max_idx]:
                max_idx = j
        array[i], array[max_idx] = array[max_idx], array[i]

print("Исходный массив:", array)