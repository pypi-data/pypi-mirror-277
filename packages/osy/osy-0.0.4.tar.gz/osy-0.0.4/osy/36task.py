class Fruit:
    def __init__(self, name, price):
        self._name = name  # Защищенный атрибут
        self._price = price  # Защищенный атрибут
        self.quantity = 0  # Обычный атрибут

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

class Apple(Fruit):
    def __init__(self, name, price, color):
        super().__init__(name, price)
        self.color = color

class Banana(Fruit):
    def __init__(self, name, price, length):
        super().__init__(name, price)
        self.length = length

class Orange(Fruit):
    def __init__(self, name, price, origin):
        super().__init__(name, price)
        self._origin = origin  # Защищенный атрибут

    def get_origin(self):
        return self._origin

# Создание объектов
apple = Apple("Apple", 2.5, "Red")
banana = Banana("Banana", 1.5, "Medium")
orange = Orange("Orange", 3.0, "Spain")

# Попытка изменить защищенный атрибут _name
apple._name = "Green Apple"
print(apple.get_name())  # Выведет "Apple"

# Попытка изменить защищенный атрибут _origin через метод
orange._origin = "Italy"
print(orange.get_origin())  # Выведет "Spain"

# Изменение обычного атрибута quantity
apple.quantity = 10
print(apple.quantity)  # Выведет 10