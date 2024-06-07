""""Описать функцию, которая:
a) присваивает параметру Е запись из самого левого листа непустого дерева
Т (лист-вершина, из которого не выходит ни одной ветви);
b) определяет число вхождений записи Е в дерево Т."""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_leftmost_leaf(tree):
    if tree is None:
        return None

    current_node = tree
    while current_node.left is not None or current_node.right is not None:
        if current_node.left:
            current_node = current_node.left
        else:
            current_node = current_node.right

    return current_node.value

def count_occurrences(tree, target):
    if tree is None:
        return 0

    count = 0
    if tree.value == target:
        count += 1

    count += count_occurrences(tree.left, target)
    count += count_occurrences(tree.right, target)

    return count

# Пример использования функций
# Создаем дерево
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(2)
root.right.right = TreeNode(5)

# Присваиваем параметру Е запись из самого левого листа непустого дерева Т
leftmost_leaf_value = find_leftmost_leaf(root)
print("Значение самого левого листа:", leftmost_leaf_value)

# Определяем число вхождений записи Е в дерево Т
occurrences_count = count_occurrences(root, leftmost_leaf_value)
print("Число вхождений записи в дерево:", occurrences_count)