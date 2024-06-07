""""Добавить элемент в начало однонаправленного связного списка."""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Пример использования
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)

print("Initial list:")
sll.display()

# Добавление элемента в начало списка
sll.prepend(5)

print("List after prepending 5:")
sll.display()