# Задача 8. Вклады
#
# Вклад в банке составляет X рублей. Ежегодно он увеличивается на P процентов, после чего дробная часть копеек
# отбрасывается. Определите, через сколько лет вклад составит не менее Y рублей.
#
# Напишите программу, которая по данным числам X, Y, P определяет, сколько лет пройдёт, прежде чем сумма достигнет
# значения Y.
import math


X = float(input('Введите сумму вклада: '))
P = float(input('Введите процентную ставку: '))
Y = float(input('Введите требуемую сумму: '))

year = 0
while X < Y:
    X += int((X / 100) * P)
    year += 1
print('Для достижения требуемой суммы понадобится', year, 'лет.')
