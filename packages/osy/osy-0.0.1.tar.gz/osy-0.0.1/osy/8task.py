class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def find_min(self):
        if not self.is_empty():
            return min(self.stack)
        else:
            return None

    def insert_zero_after_min(self):
        min_element = self.find_min()
        if min_element is not None:
            index = self.stack.index(min_element)
            self.stack.insert(index + 1, 0)

# Пример использования класса Stack
stack = Stack()
stack.push(3)
stack.push(6)
stack.push(2)
stack.push(8)
print("Стек до вставки '0':", stack.stack)

min_element = stack.find_min()
print("Минимальный элемент стека:", min_element)

stack.insert_zero_after_min()
print("Стек после вставки '0':", stack.stack)