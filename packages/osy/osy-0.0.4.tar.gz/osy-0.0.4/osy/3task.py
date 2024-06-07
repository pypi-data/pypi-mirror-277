A = [2, -5, 8, -3, 0, 7]  # Пример четного списка

def is_positive(num):
    return num > 0

def is_negative(num):
    return num < 0

positive_list = list(filter(is_positive, A))
negative_list = list(filter(is_negative, A))

print("Список положительных чисел:")
print(positive_list)

print("\nСписок отрицательных чисел:")
print(negative_list)