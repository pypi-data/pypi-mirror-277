
A = [int(x) for x in input('Введите список через пробел: ').split()]

def task1(A, el):
    deleted = []
    answer = []
    for i, val in enumerate(A):
        if val == el:
            deleted.append(val)
        else:
            answer.append(val)
    print(f"Итоговый список: {answer}")

def task2(A, el):
    deleted = []
    answer = []
    for i, val in enumerate(A):
        if val == el:
            deleted.append(i)
        else:
            answer.append(val)
    print(f"Удаленные элементы (номера): {deleted}")

run = True
while run:
    a = input("""Выберите действие: 
1. Удалить элемент из списка и вывести итоговый список.
2. Удалить элемент из списка и вывести его номер(а).
3. Конец.
""")
    if a == '1':
        el1 = int(input('Введите элемент для удаления: '))
        task1(A, el1)
    elif a == '2':
        el2 = int(input('Введите элемент для удаления: '))
        task2(A, el2)
    elif a == '3':
        print("Конец.")
        run = False
    else:
        print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")