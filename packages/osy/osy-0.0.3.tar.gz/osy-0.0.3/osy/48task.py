""""Дан список целых чисел. При помощи механизма map/filter/reduce
рассчитать разность со значением 10 для каждого из чисел списка и получить
сумму тех значений, величина которых меньше 0."""
from functools import reduce

a = [int(i) for i in input().split(' ')]
remainders = list(map(lambda x: x - 10, a))
filtered_remainders = list(filter(lambda x: x < 0, remainders))
product_of_remainders = reduce(lambda x, y: x + y, filtered_remainders)
print(product_of_remainders)