""""Даны 2 списка: перечень товаров, производимых Концернами BORK и
PHILIPS. Создать список товаров, выпускаемых как одной, так и другой фирмой.
Результат вывести в веб-интерфейс при помощи фреймворка Flask. Базу данных
можно использовать по желанию, дизайн не обязателен: достаточно обычных
кнопок/списков."""

"""
Вот примерный код на Python с использованием Flask для выполнения задачи:

1. Установите Flask, если у вас его нет. Выполните в терминале команду:
```
pip install Flask
```

2. Создайте файл app.py и добавьте в него следующий код:

```python
from flask import Flask, render_template

app = Flask(__name__)

# Списки товаров BORK и PHILIPS
bork_products = ["Товар 1", "Товар 2", "Товар 3"]
philips_products = ["Товар 3", "Товар 4", "Товар 5"]

# Находим товары, выпускаемые обеими концернами
common_products = list(set(bork_products) & set(philips_products))

@app.route('/')
def index():
    return render_template('index.html', common_products=common_products)

if __name__ == '__main__':
    app.run(debug=True)
```

3. Создайте шаблон index.html в папке templates вашего проекта и добавьте следующий код для отображения списка товаров на веб-странице:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Common Products</title>
</head>
<body>
    <h1>Список товаров, выпускаемых как BORK, так и PHILIPS:</h1>
    <ul>
        {% for product in common_products %}
            <li>{{ product }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

4. Запустите ваше Flask-приложение, выполнив в терминале команду:
```
python app.py
```

5. Откройте браузер и перейдите по адресу http://127.0.0.1:5000/ чтобы увидеть список товаров, выпускаемых как BORK, так и PHILIPS.

Это базовый пример использования Flask для реализации вашей задачи. Вы можете доработать код шаблона и функциональности при необходимости."""
