""""Даны 2 списка: перечень товаров и фамилии покупателей. Каждый n-й
покупатель покупает m-й товар. Вывести список покупок."""

def create_purchase_list(products, customers):
    """
    Создает список покупок, сопоставляя каждого n-го покупателя с m-ым товаром.

    :param products: Список товаров.
    :param customers: Список покупателей.
    :return: Список покупок.
    """
    purchase_list = []

    # Найдем минимальную длину списка, чтобы не выйти за пределы
    min_length = min(len(products), len(customers))

    for i in range(min_length):
        purchase = f"{customers[i]} покупает {products[i]}"
        purchase_list.append(purchase)

    return purchase_list

# Пример использования функции
products = ["Хлеб", "Молоко", "Сыр", "Яблоки", "Шоколад"]
customers = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов"]

purchase_list = create_purchase_list(products, customers)

for purchase in purchase_list:
    print(purchase)