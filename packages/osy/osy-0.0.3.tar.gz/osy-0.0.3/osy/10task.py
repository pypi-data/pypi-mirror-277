def not_none(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result is None:
            raise ValueError("Функция вернула значение None")
        return result
    return wrapper

# Пример использования декоратора
@not_none
def example_function(value):
    if value:
        return value
    else:
        return None

try:
    print(example_function("Hello"))
    print(example_function(None))
except ValueError as e:
    print("Ошибка:", e)