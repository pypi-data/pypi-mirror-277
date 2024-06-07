""""Дано предложение без знаков препинания. Превратить предложение в
список слов. При помощи механизма map/filter/reduce найти количество слов,
длина которых больше 4 и склеить их в одну строку"""

from functools import reduce

# Получаем предложение от пользователя
sentence = input("Введите предложение: ")

# Превращаем предложение в список слов
words = sentence.split()

# Используем map для создания списка кортежей (слово, длина слова)
words_with_lengths = list(map(lambda word: (word, len(word)), words))

# Фильтруем слова длиной больше 4
filtered_words = list(filter(lambda x: x[1] > 4, words_with_lengths))

# Извлекаем только слова из отфильтрованных кортежей
filtered_words_only = list(map(lambda x: x[0], filtered_words))

# Склеиваем отфильтрованные слова в одну строку
result = reduce(lambda x, y: x + y, filtered_words_only)

# Выводим результат
print(f"Склеенные слова длиной больше 4: {result}")