""""13. Создать класс стек. Использовать способ реализации стека через list.
Удалить минимальный элемент стека. (20 баллов)"""

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def find_min(self):
        if not self.is_empty():
            return min(self.stack)
        else:
            return None

    def remove_min(self):
        if not self.is_empty():
            min_element = self.find_min()
            self.stack = [x for x in self.stack if x != min_element]
            print(self.stack)
        else:
            print("Стек пустой")

# Пример использования
stack = Stack()
stack.push(4)
stack.push(5)
stack.push(4)
stack.push(7)

stack.remove_min()