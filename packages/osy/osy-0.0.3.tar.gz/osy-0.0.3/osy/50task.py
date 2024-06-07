""""В одномерном массиве целых чисел найти количество пар элементов
разного знака. (пара — это два рядом стоящих элемента)."""

def count_opposite_sign_pairs(arr):
    count = 0
    for i in range(1, len(arr)):
        if arr[i] * arr[i-1] < 0:
            count += 1
    return count

# Ввод данных от пользователя
try:
    a = [int(i) for i in input("Введите целые числа через пробел: ").split()]
    result = count_opposite_sign_pairs(a)
    print(f"Количество пар элементов разного знака: {result}")
except ValueError:
    print("Ошибка: Введите только целые числа.")