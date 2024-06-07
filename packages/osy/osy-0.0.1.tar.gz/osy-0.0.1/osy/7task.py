from functools import reduce

# Предложение без знаков препинания
sentence = "Дано предложение без знаков препинания"

# Разделение предложения на список слов
words = sentence.split()

# Отброс последней буквы у каждого слова и объединение слов длиной более 5 символов
result = reduce(lambda x, y: x + y, map(lambda word: word[:-1], filter(lambda word: len(word) > 5, words)))

print(result)
