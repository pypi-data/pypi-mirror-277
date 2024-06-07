"""
Создайте класс Заказ(Order), у которого есть свойства кодтовара(code), цена(price), количество(count) и методы _init и str. Создайте 2 класса-потомка: Опт(Opt) и Розница(Retail). В этих классах создайте методы init, str и суммазаказа (summa), позволяющий узнать стоимость заказа. Для опта стоимость единицы товара составляет 95% от цены, а при покупке более 500 штук – 90% цены. В розницу стоимость единицы товара составляет 100% цены. Стоимость заказа равна произведению цены на количество. Создайте список, содержащий по 2 объекта каждого класса (Order, Opt, Retail). Для этого списка: • выведите информацию о каждом объекте с помощью метода _str; • найдите общую стоимость заказов для объектов Opt и Retail. (20 баллов)
"""
class Order:
    def __init__(self, code, price, count):
        self.code = code
        self.price = price
        self.count = count

    def __str__(self):
        return f"Товар: {self.code}, Цена: {self.price}, Количество: {self.count}"

class Opt(Order):
    def __init__(self, code, price, count):
        super().__init__(code, price, count)

    def summa(self):
        if self.count > 500:
            return self.price * self.count * 0.9
        else:
            return self.price * self.count * 0.95

class Retail(Order):
    def __init__(self, code, price, count):
        super().__init__(code, price, count)

    def summa(self):
        return self.price * self.count

# Создание объектов
orders = [
    Order("Товар1", 100, 200),
    Order("Товар2", 50, 300),
    Opt("Товар3", 100, 600),
    Opt("Товар4", 80, 400),
    Retail("Товар5", 120, 150),
    Retail("Товар6", 70, 250)
]

# Вывод информации о каждом объекте
for order in orders:
    print(order)
    if isinstance(order, Opt) or isinstance(order, Retail):
        print(f"Стоимость заказа: {order.summa()}")

# Вычисление общей стоимости заказов для объектов Opt и Retail
total_cost = sum(order.summa() for order in orders if isinstance(order, Opt) or isinstance(order, Retail))
print(f"\nОбщая стоимость заказов: {total_cost}")