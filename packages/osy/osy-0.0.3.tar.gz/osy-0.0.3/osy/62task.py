""""Дан список с перечнем товаров. Выбрать все товары, изготовленные
фирмой Bosh и создать из них новый список."""

# Исходный список товаров
products = [
    {"name": "Washing Machine", "manufacturer": "Bosh", "price": 300},
    {"name": "Refrigerator", "manufacturer": "Samsung", "price": 500},
    {"name": "Microwave", "manufacturer": "Bosh", "price": 150},
    {"name": "Vacuum Cleaner", "manufacturer": "LG", "price": 200},
    {"name": "Dishwasher", "manufacturer": "Bosh", "price": 400},
    {"name": "Oven", "manufacturer": "Electrolux", "price": 350}
]

# Фильтрация товаров, изготовленных фирмой Bosh
bosh_products = [product for product in products if product["manufacturer"] == "Bosh"]

# Вывод нового списка товаров, изготовленных фирмой Bosh
print("Products manufactured by Bosh:")
for product in bosh_products:
    print(product)