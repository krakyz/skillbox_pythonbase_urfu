# Математик Саша пишет программу, которая должна строить график функции y = |x|. Для этого ему нужно найти модуль очередного числа x, то есть если число x отрицательное, то перевести его в положительное.
# Напишите программу, которая выводит на экран модуль введённого числа.
# Пример:
# Ввели 5, ответ 5
# Ввели −7, ответ 7

Подсказка: достаточно в некоторых случаях переприсвоить переменную со знаком минус.

x = int(input('Введите X: '))

if x < 0:
    x_res = x * -1
else:
    x_res = x

print('Вы ввели', x, ', ответ', x_res)
