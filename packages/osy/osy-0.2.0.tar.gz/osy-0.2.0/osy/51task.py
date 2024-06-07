""""Задание: построить базовый класс с указанными в таблице полями и 
методами:
- конструктор; - функция, которая определяет «качество» объекта – Q по 
заданной формуле; - метод вывода информации об объекте.
Построить дочерний класс (класс-потомок), который содержит:
- дополнительное поле P;
- функция, которая определяет «качество» объекта дочернего класса – Qp и 
перегружает функцию качества родительского класса (Q), выполняя вычисление по 
новой формуле.
Создать проект для демонстрации работы: ввод и вывод информации об 
объектах классов. (20 баллов)
Поля и методы базового класса Поля и методы дочернего класса
Компьютер:
- наименование процессора;
- тактовая частота процессора (МГц);
- объем оперативной памяти (Мб);
- Q = (0,1·частота) + память


P: объем накопителя SSD (Гб)
- Qp = Q +0,5P"""""

class Computer:
    def __init__(self, processor_name, clock_speed, ram):
        self.processor_name = processor_name
        self.clock_speed = clock_speed
        self.ram = ram

    def quality(self):
        return (0.1 * self.clock_speed) + self.ram

    def display_info(self):
        print(f"Processor Name: {self.processor_name}")
        print(f"Clock Speed (MHz): {self.clock_speed}")
        print(f"RAM (MB): {self.ram}")
        print(f"Quality (Q): {self.quality()}")

class AdvancedComputer(Computer):
    def __init__(self, processor_name, clock_speed, ram, ssd):
        super().__init__(processor_name, clock_speed, ram)
        self.ssd = ssd

    def quality(self):
        base_quality = super().quality()
        return base_quality + 0.5 * self.ssd

    def display_info(self):
        super().display_info()
        print(f"SSD (GB): {self.ssd}")
        print(f"Quality with SSD (Qp): {self.quality()}")

# Пример использования классов
if __name__ == "__main__":
    # Создание объекта базового класса
    computer = Computer("Intel i5", 3200, 8192)
    print("Basic Computer Info:")
    computer.display_info()

    print("\nAdvanced Computer Info:")
    # Создание объекта дочернего класса
    advanced_computer = AdvancedComputer("Intel i7", 3600, 16384, 512)
    advanced_computer.display_info()