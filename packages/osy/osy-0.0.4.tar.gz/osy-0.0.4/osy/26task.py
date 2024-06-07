"""
Дан список А3, состоящий из четного количества элементов. Используя функцию(функции) высшего порядка разбейте его на списки В, С так, чтобы в одном были положительные элементы, а в другом отрицательные. (20 баллов)
"""
A3 = [5, -3, 8, -2, 10, -7]

def divide_list(lst, condition):
    return [item for item in lst if condition(item)]

positive_numbers = divide_list(A3, lambda x: x > 0)
negative_numbers = divide_list(A3, lambda x: x < 0)

print("Список положительных элементов В:", positive_numbers)
print("Список отрицательных элементов С:", negative_numbers)