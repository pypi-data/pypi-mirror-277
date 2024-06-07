""""Вершины дерева вещественные числа. Описать функцию, которая
вычисляет среднее арифметическое всех вершин
дерева. Результат вывести в веб-интерфейс при помощи фреймворка Django. Базу
данных можно использовать по желанию, дизайн не обязателен: достаточно
обычных кнопок/списков."""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def calculate_average(node):
    if node is None:
        return (0, 0)  # Сумма и количество вершин

    left_sum, left_count = calculate_average(node.left)
    right_sum, right_count = calculate_average(node.right)

    total_sum = left_sum + right_sum + node.value
    total_count = left_count + right_count + 1

    return (total_sum, total_count)

# Пример использования функции
# Создаем дерево
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

total_sum, total_count = calculate_average(root)
average = total_sum / total_count

print("Среднее арифметическое всех вершин дерева:", average)