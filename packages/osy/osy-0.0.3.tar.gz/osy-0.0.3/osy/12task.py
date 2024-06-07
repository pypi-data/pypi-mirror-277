""""12. Реализовать декоратор с именем print_type, выводящий на печать тип
значения, возвращаемого декорируемой функцией. (20 баллов)"""

def print_type(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Тип возвращаемого значения: {type(result).__name__}")
        return result
    return wrapper

@print_type
def add(a, b):
    return a + b

result = add('a', 'b')