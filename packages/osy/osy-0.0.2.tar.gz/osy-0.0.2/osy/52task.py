""""Создать иерархию классов для фруктов, продающихся в магазине.
Иерархия должна содержать не менее 3 классов. Объекты должны содержать не
менее 2-х атрибутов и 2-х методов. Реализовать механизм автоматического
подсчета количества всех созданных фруктов и автоматического присвоения
каждому фрукту уникального идентификатора. Необходимо заполнить список
представителями всех классов (всего не менее 5 объектов) и продемонстрировать
работу созданного механизма."""

class Fruit:
    total_fruits = 0

    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
        Fruit.total_fruits += 1
        self.id = Fruit.total_fruits

    def display_info(self):
        print(f"ID: {self.id}, Color: {self.color}, Weight: {self.weight}g")

    @classmethod
    def get_total_fruits(cls):
        return cls.total_fruits


class Apple(Fruit):
    def __init__(self, color, weight, variety):
        super().__init__(color, weight)
        self.variety = variety

    def display_info(self):
        super().display_info()
        print(f"Variety: {self.variety}")


class Plum(Fruit):
    def __init__(self, color, weight, ripeness):
        super().__init__(color, weight)
        self.ripeness = ripeness

    def display_info(self):
        super().display_info()
        print(f"Ripeness: {self.ripeness}")


class Peach(Fruit):
    def __init__(self, color, weight, sweetness):
        super().__init__(color, weight)
        self.sweetness = sweetness

    def display_info(self):
        super().display_info()
        print(f"Sweetness: {self.sweetness}")


# Пример использования классов
if __name__ == "__main__":
    fruits = [
        Apple("Red", 150, "Gala"),
        Apple("Green", 130, "Granny Smith"),
        Plum("Purple", 50, "Ripe"),
        Plum("Yellow", 55, "Unripe"),
        Peach("Orange", 200, "Very Sweet")
    ]

    for fruit in fruits:
        fruit.display_info()
        print()

    print(f"Total number of fruits created: {Fruit.get_total_fruits()}")
