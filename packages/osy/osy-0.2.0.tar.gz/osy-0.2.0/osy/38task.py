def f(x):
    # Здесь определите вашу функцию f(x)
    return x ** 2 - 4  # Пример: уравнение x^2 - 4 = 0


def Root(a, b, epsilon):
    if (b - a) < epsilon:
        return (a + b) / 2

    c = (a + b) / 2
    if f(a) * f(c) < 0:
        return Root(a, c, epsilon)
    else:
        return Root(c, b, epsilon)


# Заданный отрезок [a, b] и точность epsilon
a = 0
b = 3
epsilon = 0.0001

# Находим корень уравнения f(x) = 0 на отрезке [a, b] с заданной точностью
root = Root(a, b, epsilon)
print("Приближенное значение корня уравнения: ", root)