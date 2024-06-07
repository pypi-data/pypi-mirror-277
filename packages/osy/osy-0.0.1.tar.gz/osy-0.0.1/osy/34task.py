def Fact(N):
    if N == 0:
        return 1
    else:
        return N * Fact(N - 1)

def Fact2(N):
    if N <= 0:
        return 1
    elif N == 1:
        return 1
    else:
        return N * Fact2(N - 2)

# Пример вызова функций для вычисления факториала и двойного факториала
N = 5
factorial_N = Fact(N)
double_factorial_N = Fact2(N)

print(f"Факториал {N}! = {factorial_N}")
print(f"Двойной факториал {N}!! = {double_factorial_N}")