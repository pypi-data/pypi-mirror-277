""""Реализовать функцию st_reverse(a_string), которая при помощи стека
инвертирует строку (меняет порядок букв на обратный). Пример: st_reverse(‘abcd’)
-> ‘dcba’."""


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


def st_reverse(a_string):
    stack = Stack()

    # Помещаем все символы строки в стек
    for char in a_string:
        stack.push(char)
    # Извлекаем символы из стека и собираем их в обратном порядке
    reversed_string = ''
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string


# Пример использования
input_string = 'abcd'
reversed_string = st_reverse(input_string)
print(f"Original string: {input_string}")
print(f"Reversed string: {reversed_string}")