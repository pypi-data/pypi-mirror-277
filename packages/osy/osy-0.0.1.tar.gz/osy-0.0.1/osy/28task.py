"""
Дан список S состоящий из N различных элементов. Вывести индексы четных элементов списка. Использовать функции высшего порядка. (20 баллов)
"""

S = [3, 7, 10, 4, 5, 8, 2, 6]

def get_even_indices(lst):
    return [index for index, item in enumerate(lst) if item % 2 == 0]

even_indices = get_even_indices(S)

print("Индексы четных элементов списка S:", even_indices)