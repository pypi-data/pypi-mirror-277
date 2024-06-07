""""Реализовать декоратор с именем not_sum, который генерирует
исключительную ситуацию, если декорируемая функция вернула отрицательное
значение суммы трех чисел. (20 баллов)"""

class NegativeSum(Exception):
    pass

def not_sum(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (int,float)) and result < 0:
            raise NegativeSum("Отрицательное значение суммы трех чисел")
        return result
    return wrapper

@not_sum
def sum_of_three(a,b,c):
    return a+b+c

try:
    print(sum_of_three(1,2,3))
    print(sum_of_three(-1,-2,-3))
except NegativeSum as e:
    print(e)


