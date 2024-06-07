""""Реализовать двоичное дерево в виде связанных объектов (реализовать
класс для элементов двоичного дерева) и реализовать симметричную процедуру
обхода двоичного дерева в виде рекурсивной функции. """

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def in_order_traversal(self):
        return self._in_order_recursive(self.root)

    def _in_order_recursive(self, node):
        result = []
        if node:
            result += self._in_order_recursive(node.left)
            result.append(node.value)
            result += self._in_order_recursive(node.right)
        return result

# Пример использования
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

print("In-order traversal:", tree.in_order_traversal())