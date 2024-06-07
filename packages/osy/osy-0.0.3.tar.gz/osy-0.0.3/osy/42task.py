from functools import reduce

numbers = map(int, input("Ввод списка через пробел: ").split())
def funk(num):
    return num % 7
filtered_numbers = filter(lambda x: x > 4, map(funk, numbers))
result = reduce(lambda x, y: x * y, filtered_numbers)
print(result)
