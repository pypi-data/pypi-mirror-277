""""Дан список целых чисел. При помощи механизма map/filter/reduce
рассчитать остаток от деления на 17 для каждого из чисел списка и получить
произведение тех остатков, величина которых меньше 7. (20 баллов)"""
from functools import reduce

a = [int(i) for i in input().split(' ')]
remainders = list(map(lambda x: x % 17, a))
filtered_remainders = list(filter(lambda x: x < 7, remainders))
product_of_remainders = reduce(lambda x, y: x * y, filtered_remainders)
print(product_of_remainders)