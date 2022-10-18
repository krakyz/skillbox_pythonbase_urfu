# Вы пишите компьютерную игру с текстовой графикой, вам поручили написать генератор ландшафта.
#
# Напишите программу, которая получает на вход число N и выводит на экран числа в виде «ямы» вот так:
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345

depth = int(input('Введите число: '))

for row in range(depth):
    for left_number in range(depth, depth - row - 1, -1):
        print(left_number, end='')
    dots = 2 * (depth - row - 1)
    print('.' * dots, end='')
    for right_number in range(depth - row, depth + 1):
        print(right_number, end='')
    dots -= 2
    print()

