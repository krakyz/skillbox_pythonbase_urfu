# Задача 5. Счастливый билетик
#
# В старину, когда даже в столице билеты в общественном транспорте выдавали контролёры, существовало поверье: если на
# билете сумма первых трёх цифр в номере билета равна сумме последних трёх, то это к удаче.
#
# Напишите программу, которая получала бы на входе номер билета из четного количества цифр и выводила, счастливый это
# билет или нет. К примеру, билеты 666 666 и 252 135 — счастливые, а 123 456 — нет.

number = int(input('Введите номер билета: '))

while number > 0:
    number_copy = number
    counter = 0
    while number_copy > 0:
        number_copy //= 10
        counter += 1
    if counter % 2 != 0:
        print('Количство цифр нечетное. Вычисление невозможно.')

    first_half = 0
    second_half = 0
    counter_copy = counter
    while counter_copy > counter / 2:
        second_half += number % 10
        number //= 10
        counter_copy -= 1
    while counter_copy > 0:
        first_half += number % 10
        number //= 10
        counter_copy -= 1

if first_half == second_half:
    print('Вам выпал счастливый билет!')
else:
    print('Увы. Вам не повезло.')

