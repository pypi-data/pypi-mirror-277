""""Дан двунаправленный связный список. Вставить элемент после n-го
элемента списка."""


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

    def insert_after_n(self, n, data):
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
            print(f"Cannot insert after {n}-th element as the list has fewer elements.")
            return

        # Создаем новый узел
        new_node = Node(data)

        # Вставляем новый узел после текущего
        new_node.next = current.next
        new_node.prev = current

        if current.next:
            current.next.prev = new_node

        current.next = new_node

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

n = 2  # Вставка после 2-го элемента (0-based index)
data_to_insert = 99

dll.insert_after_n(n, data_to_insert)

print(f"List after inserting {data_to_insert} after {n}-th element:")
dll.display()
