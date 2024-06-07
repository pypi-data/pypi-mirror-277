""""Соединить два однонаправленных связных списка."""

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

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def extend(self, other_list):
        if self.head is None:
            self.head = other_list.head
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = other_list.head

# Пример использования
list1 = SinglyLinkedList()
list1.append(1)
list1.append(2)
list1.append(3)

list2 = SinglyLinkedList()
list2.append(4)
list2.append(5)
list2.append(6)

print("First list:")
list1.display()

print("Second list:")
list2.display()

# Соединение двух списков
list1.extend(list2)

print("Combined list:")
list1.display()