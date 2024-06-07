"""
Дан однонаправленный связный список. Вставить элемент после n-го элемента списка. (20 баллов)
"""
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def insert_after_n(head, n, new_data):
    if head is None:
        return None

    current = head
    count = 1

    while current is not None and count < n:
        current = current.next
        count += 1

    if current is None:
        print("The list has less than", n, "elements")
        return head

    new_node = Node(new_data)
    new_node.next = current.next
    current.next = new_node

    return head

# Пример использования
def print_list(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()

if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    print("Initial list:")
    print_list(head)

    head = insert_after_n(head, 2, 4)

    print("List after inserting element:")
    print_list(head)