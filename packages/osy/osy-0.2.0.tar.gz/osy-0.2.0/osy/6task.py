class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def remove_every_second_element(self):
        temp_stack = Stack()
        is_second = False

        while not self.is_empty():
            item = self.pop()
            if is_second:
                is_second = False
            else:
                temp_stack.push(item)
                is_second = True

        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

# Пример использования
stack = Stack()
for i in range(1, 11):
    stack.push(i)

print("Исходный стек:")
print(stack.items)

stack.remove_every_second_element()

print("Стек после удаления каждого второго элемента:")
print(stack.items)