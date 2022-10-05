# Задача 8. Сумма ряда
# Дано натуральное число n. Напишите программу для вычисления следующей суммы ряда (начиная с единицы):
# S = 1 - 1/2 +1/4 - 1/8 + ... + (-1)^n * 1/2^n Член ряда

n = int(input('Введите натуральное число: '))

S = x = 1
for i in range(1, n+1):
    x = ((-1) ** i) / (2 ** i)
    S += x
print(S)