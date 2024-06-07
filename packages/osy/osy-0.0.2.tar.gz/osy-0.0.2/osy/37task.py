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