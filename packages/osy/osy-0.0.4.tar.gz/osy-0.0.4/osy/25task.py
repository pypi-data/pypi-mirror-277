"""
Создать класс стек. Использовать способ реализации стека через list. Сформировать стек с элементами - строками. Прочитать три нижних элемента стека и поменять местами верхний и нижний элементы. (20 баллов)
"""
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

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

# Создание экземпляра класса Stack
stack = Stack()

# Добавление элементов-строк в стек
stack.push("One")
stack.push("Two")
stack.push("Three")
stack.push("Four")
stack.push("Five")

# Чтение трех нижних элементов стека
for _ in range(3):
    print(f"Нижний элемент стека: {stack.pop()}")

# Меняем местами верхний и нижний элементы стека
top = stack.pop()
bottom = stack.pop()
stack.push(top)
stack.push(bottom)

# Вывод стека после изменения местами элементов
print("Стек после замены элементов:")
while not stack.is_empty():
    print(stack.pop())