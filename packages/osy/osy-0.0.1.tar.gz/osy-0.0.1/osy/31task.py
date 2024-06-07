""""31. Реализовать однонаправленный связанный список (реализовать класс для
элементов списка). Преобразовать строку 'Eeny, meeny, miney, moe; Catch a tiger by
his toe.' в связный список символов строки и удалить из него все элементы
содержащие гласные буквы. (20 баллов)"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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

def remove_vowels_from_linked_list(linked_list):
    vowels = "aeiouAEIOU"
    current = linked_list.head
    prev = None

    while current:
        if current.data in vowels:
            if prev is None:
                linked_list.head = current.next
            else:
                prev.next = current.next
        else:
            prev = current
        current = current.next

# Создаем связанный список из строки
string = 'Eeny, meeny, miney, moe; Catch a tiger by his toe.'
char_list = LinkedList()
for char in string:
    char_list.append(char)

# Удаляем гласные буквы из связанного списка
remove_vowels_from_linked_list(char_list)
# Выводим итоговый связанный список
char_list.display()