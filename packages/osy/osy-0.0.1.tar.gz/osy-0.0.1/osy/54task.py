"""". В одномерном массиве (array) целых чисел найти количество пар, модуль
разности элементов которых больше 10. (пара — это два рядом стоящих элемента)."""

def count_modul_more10_pairs(arr):
    count = 0
    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i-1]) > 10:
            count += 1
    return count

# Ввод данных от пользователя
try:
    a = [int(i) for i in input("Введите целые числа через пробел: ").split()]
    result = count_modul_more10_pairs(a)
    print(f"Количество пар с модулем разности больше 10: {result}")
except ValueError:
    print("Ошибка: Введите только целые числа.")