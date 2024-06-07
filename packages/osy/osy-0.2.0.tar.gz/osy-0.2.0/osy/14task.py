def binary_addition(bin1, bin2):
    if not bin1:
        return bin2
    if not bin2:
        return bin1

    if bin1[-1] == '1' and bin2[-1] == '1':
        return binary_addition(binary_addition(bin1[:-1], '1') + '0', bin2[:-1])
    elif bin1[-1] == '0' and bin2[-1] == '0':
        return binary_addition(bin1[:-1], bin2[:-1]) + '0'
    else:
        return binary_addition(bin1[:-1], bin2[:-1]) + '1'

# Пример использования
bin_num1 = '1010'  # Положительное число в двоичной системе
bin_num2 = '1101'  # Отрицательное число в двоичной системе

result = binary_addition(bin_num1, bin_num2)
print(f"Сумма чисел {bin_num1} и {bin_num2} в двоичной системе: {result}")