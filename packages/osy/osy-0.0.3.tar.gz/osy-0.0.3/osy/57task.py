""""Дан двунаправленный связный список. Удалить n-ый элемент списка."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
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
        new_node.prev = last

    def delete_nth(self, n):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        count = 0

        # Пройдем по списку до n-го элемента
        while current and count < n:
            current = current.next
            count += 1

        # Если текущий элемент не найден, значит n больше длины списка
        if current is None:
            print(f"Cannot delete {n}-th element as the list has fewer elements.")
            return

        # Если текущий элемент является головным узлом
        if current.prev is None:
            self.head = current.next
            if self.head:
                self.head.prev = None
        else:
            current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev

        # Удаляем текущий узел
        del current

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Пример использования
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)

print("Initial list:")
dll.display()

n = 2  # Удаление 2-го элемента (0-based index)

dll.delete_nth(n)

print(f"List after deleting {n}-th element:")
dll.display()
