""""Дано два однонаправленных связных списка. Создать список,
содержащий элементы общие для двух списков. (20 баллов)"""

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


def find_common_elements(head1, head2):
    # Используем множество для хранения элементов первого списка
    elements_set = set()
    current = head1
    while current:
        elements_set.add(current.value)
        current = current.next

    # Создаем новый список для общих элементов
    dummy_head = ListNode()
    current_common = dummy_head

    # Проверяем элементы второго списка на наличие в множестве
    current = head2
    while current:
        if current.value in elements_set:
            current_common.next = ListNode(current.value)
            current_common = current_common.next
            # Удаляем элемент из множества, чтобы избежать дублирования
            elements_set.remove(current.value)
        current = current.next

    return dummy_head.next


# Пример использования
list1_values = [1, 2, 3, 4, 5]
list2_values = [3, 4, 5, 6, 7]

head1 = create_linked_list(list1_values)
head2 = create_linked_list(list2_values)

print("List 1:")
print_linked_list(head1)

print("List 2:")
print_linked_list(head2)

common_head = find_common_elements(head1, head2)

print("Common elements:")
print_linked_list(common_head)