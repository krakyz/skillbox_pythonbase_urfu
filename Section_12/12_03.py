# Задача 3. Апгрейд калькулятора
#
# Степан, как и большая часть населения планеты, для расчёта суммы и разности чисел использует калькулятор. Однако в
# работе ему нужно делать не только обычные действия вроде сложения и вычитания, а делать что-то вручную он уже
# устал. Поэтому Степан решил немного расширить функционал своего калькулятора.
#
# Напишите программу, запрашивающую у пользователя число и действие, которое нужно с ним сделать: вывести сумму его
# цифр, максимальную или минимальную цифру. Каждое действие оформите в виде отдельной функции, а основную программу
# зациклите.

import math


def actions():
    print('Доступные действия:\n1 — сумма цифр числа\n2 — максимальная цифра числа\n3 — минимальная цифра числа')
    action = int(input('\nВведите действие: '))
    if action == 1:
        sumDigit()
    elif action == 2:
        maxDigit()
    elif action == 3:
        minDigit()
    else:
        print('Ошибка ввода.\n')
        actions()


def toActions(number):
    if number == 0:
        print()
        actions()


def sumDigit():
    number = int(input('\nВыбранное действие — сумма цифр числа. Введите 0 для выхода в меню.\nВведите число: '))
    toActions(number)
    summ = 0
    for number in range(number + 1):
        summ += number
    print(f'Сумма чисел от 1 до {number} равна {summ}')
    print()


def maxDigit():
    number = int(
        input('\nВыбранное действие — максимальная цифра числа. Введите 0 для выхода в меню.\nВведите число: '))
    toActions(number)
    max_digit = 0
    number_copy = number
    while number_copy != 0:
        current_digit = number_copy % 10
        if current_digit > max_digit:
            max_digit = current_digit
        number_copy //= 10
    print(f'Максимальная цифра числа {number} равна {max_digit}')
    print()


def minDigit():
    number = int(
        input('\nВыбранное действие — минимальная цифра числа. Введите 0 для выхода в меню.\nВведите число: '))
    toActions(number)
    min_digit = math.inf
    number_copy = number
    while number_copy != 0:
        current_digit = number_copy % 10
        if current_digit < min_digit:
            min_digit = current_digit
        number_copy //= 10
    print(f'Минимальная цифра числа {number} равна {min_digit}')
    print()


while True:
    actions()
