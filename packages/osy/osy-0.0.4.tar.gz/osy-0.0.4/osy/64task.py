"""Даны 2 списка с фамилиями студентов 2-х групп. Перевести n студентов
из 1-й группы во 2-ю. Число пересчета - k."""


def transfer_students(group1, group2, n, k):
    """
    Переводит n студентов из первой группы во вторую с учетом числа пересчета k.

    :param group1: Список студентов первой группы.
    :param group2: Список студентов второй группы.
    :param n: Количество студентов для перевода.
    :param k: Число пересчета.
    :return: Обновленные списки групп.
    """
    if n <= 0 or k <= 0:
        raise ValueError("Число студентов для перевода и число пересчета должны быть положительными")

    transferred_count = 0
    index = 0

    while transferred_count < n and group1:
        # Находим индекс студента для перевода с учетом числа пересчета k
        index = (index + k - 1) % len(group1)

        # Переносим студента из первой группы во вторую
        student = group1.pop(index)
        group2.append(student)

        # Увеличиваем счетчик переведенных студентов
        transferred_count += 1

    return group1, group2


# Пример использования функции
group1 = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов"]
group2 = ["Александров", "Борисов", "Васильев"]

n = 3
k = 2

updated_group1, updated_group2 = transfer_students(group1, group2, n, k)

print("Обновленная первая группа:", updated_group1)
print("Обновленная вторая группа:", updated_group2)