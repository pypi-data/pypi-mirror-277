def dec(a, b):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            if result > 0:
                result += a
            else:
                result -= b
            return result
        return wrapper
    return decorator

# Пример использования декоратора
@dec(a=5, b=3)
def sum_numbers(*args):
    return sum(args)

# Проверка работы декорированной функции
result1 = sum_numbers(1, 2, 3, 4)  # Сумма = 10, положительная
result2 = sum_numbers(-1, -2, -3)  # Сумма = -6, отрицательная

print("Результат с положительной суммой:", result1)
print("Результат с отрицательной суммой:", result2)