class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def swap_first_and_last(self):
        if len(self.items) < 2:
            return

        first_element = self.items[0]
        self.items[0] = self.items[-1]
        self.items[-1] = first_element


# Пример использования
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Стек до замены:")
print(stack.items)

stack.swap_first_and_last()

print("\nСтек после замены:")
print(stack.items)