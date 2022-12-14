# Задача 6. Метеостанция
# Что нужно сделать
#
# Сотрудники международной метеостанции должны каждый день передавать показания градусов по шкалам и Цельсия,
# и Фаренгейта.
#
# Напишите программу, которая принимает на вход три целых числа в градусах Цельсия: нижняя граница
# температуры, верхняя граница температуры и шаг.
#
# Программа выводит на экран таблицу соответствия градусов Цельсия градусам Фаренгейта от нижней до верхней границы с
# указанным шагом. Обеспечьте контроль ввода. Верхняя граница должна печататься, даже если последний шаг
# "перепрыгнул" ее. Известно, что 0С соответствует 32F, а каждый градус Цельсия эквивалентен 1.8 градусам Фаренгейта.
#
# Пример:
# Ввод:
# Нижняя граница: 0
# Верхняя граница: 50
# Шаг: 20
# Вывод:
# C   F
# 0   32
# 20  68
# 40  104
# 50  122

import math

lower_limit = int(input('Нижняя граница: '))
upper_limit = int(input('Верхняя граница: '))
step = int(input('Шаг: '))

iterations = math.ceil((lower_limit + upper_limit) / step)

print('C\tF')
for C in range(lower_limit, upper_limit, step):
    if C == 0:
        F = 32
    else:
        F = int(32 + C * 1.8)
    print(f'{C}\t{F}')
if upper_limit % step != 0:
    C = upper_limit
    F = int(32 + C * 1.8)
    print(f'{C}\t{F}')
