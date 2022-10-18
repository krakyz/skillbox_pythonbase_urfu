# Задача 4. Крест
#
# Напишите программу, которая выводит на экран крест из символов ^
#
# ^         ^
#   ^     ^
#     ^ ^
#     ^ ^
#   ^     ^
# ^         ^
#
# (символы выводятся по диагоналям воображаемого квадрата).

N = int(input('Введите длину стороны квадрата: '))

for row in range(N + 1):
    for column in range(N + 1):
        if column == row:
            print('^', end=' ')
        elif column == -row + N:
            print('^', end=' ')
        else:
            print(' ', end=' ')
    print()
