class Salary:
    def __init__(self, oklad, procent):
        self.oklad = oklad
        self.procent = procent

    def calculate_tax(self):
        nalog = self.oklad * self.procent / 100
        return nalog

    def calculate_take_home_pay(self):
        nalog = self.calculate_tax()
        summa = self.oklad - nalog
        return summa

# Пример использования класса
oklad = 50000  # Пример величины оклада
procent = 13  # Пример ставки подоходного налога

employee_salary = Salary(oklad, procent)
nalog = employee_salary.calculate_tax()
summa = employee_salary.calculate_take_home_pay()

print(f"Размер налога: {nalog}")
print(f"Сумма, получаемая на руки: {summa}")