n = int(input("Введите число: ")) # Вводим число.

sum_num = 0
pr_num =  1
sq_num = 0

for i in range(1, n + 1):
    sum_num += i
    pr_num *= i
    sq_num += i**2

print(f"Сумма: {sum_num}")
print(f"Факториал числа: {pr_num}")
print(f"Сумма квадратов: {sq_num}")