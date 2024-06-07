"""
Дан кольцевой список из 20 фамилий студентов. Разбить студентов на 2 группы по 10 человек. Во вторую группу попадает каждый 11-й человек. (20 баллов)
"""
class Node:
    def init(self, surname):
        self.surname = surname
        self.next = None

class CircularList:
    def init(self):
        self.head = None

    def add(self, surname):
        if not self.head:
            self.head = Node(surname)
            self.head.next = self.head
        else:
            new_node = Node(surname)
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def split_students(self):
        current = self.head
        group1 = CircularList()
        group2 = CircularList()
        count = 0

        while count < 20:
            if count < 10:
                group1.add(current.surname)
            else:
                group2.add(current.surname)
            current = current.next
            count += 1

        return group1, group2

    def print_group(self):
        current = self.head
        while True:
            print(current.surname)
            current = current.next
            if current == self.head:
                break

# Создание кольцевого списка и добавление 20 фамилий
circular_list = CircularList()
# Пример добавления: circular_list.add("Иванов")
# Добавьте остальные 19 фамилий здесь

# Разделение студентов на группы
group1, group2 = circular_list.split_students()

# Вывод групп
print("Группа 1:")
group1.print_group()
print("Группа 2:")
group2.print_group()