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

    def remove_middle_elements(self):
        stack_length = len(self.items)
        if stack_length % 2 == 0:
            mid = stack_length // 2
            del self.items[mid - 1:mid + 1]
        else:
            mid = stack_length // 2
            del self.items[mid]

    def display(self):
        print("Current Stack:")
        for item in self.items:
            print(item)

# Пример использования
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print("Исходный стек:")
stack.display()

stack.remove_middle_elements()

print("\nСтек после удаления средних элементов:")
stack.display()