class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def delete_every_second_node(head):
    current = head

    while current is not None and current.next is not None:
        current.next = current.next.next
        current = current.next

# Функция для печати элементов связного списка
def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()

# Создание примера связного списка
head = Node(1)
current = head
for i in range(2, 11):
    current.next = Node(i)
    current = current.next

print("Исходный связный список:")
print_linked_list(head)

# Удаление каждого второго элемента из списка
delete_every_second_node(head)

print("Связный список после удаления каждого второго элемента:")
print_linked_list(head)