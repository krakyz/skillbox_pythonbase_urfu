# Задача 9. Выражение
# Дано число x. Напишите программу для вычисления следующего выражения:
# res = ((x-1)(x-3)(x-7)(x-15)...(x-63)) / ((x-2)(x-4)(x-8)(x-16)...(x-64))
#
# Обратите внимание на последовательность в числителе и знаменателе. Эта последовательность
# не является возрастающей арифметической последовательностью 1, 3, 5, 7 … 63 и 2, 4, 6, 8 … 64.

x = int(input('Введите X: '))
numerator_x = denominator_x = x

numerator_action = 0
denominator_action = 1


for i in range(6):   # будет 6 итераций
    # действие в числителе изменяется на (* 2 + 1) с каждой итерацией
    numerator_action = numerator_action * 2 + 1
    numerator_x -= numerator_action
    # действие в знаменателе изменяется на (* 2) с каждой итерацией
    denominator_action *= 2
    denominator_x -= denominator_action
x = numerator_x / denominator_x
print(f'Выражение равно {x}')
