S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Используем функцию enumerate для получения индексов и значений элементов списка
even_indices = list(map(lambda x: x[0], filter(lambda x: x[1] % 2 == 0, enumerate(S))))

print("Индексы четных элементов списка S:", even_indices)