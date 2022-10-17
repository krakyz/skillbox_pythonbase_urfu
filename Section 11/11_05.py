# Задача 5. Вот это объёмы!
#
# Для курсовой работы по физике Андрею нужно сравнить объёмы двух планет: Земли и какой-нибудь случайной,
# которая может в теории существовать в нашей вселенной. Андрей хорошо разбирается в формулах, а вот считать что-то,
# а уж тем более самому - это явно не его. Объём Земли ему известен заранее - это 10.8321 * 10^11 км3
#
# А вот объём случайной планеты ему нужно будет посчитать. Благо, у него есть формула:
#
# V = 4/3 * pi * R^3
#
# где V - это объём, π - число пи, а R - радиус планеты.
#
# Напишите программу, которая получает на вход радиус случайной планеты и выводит на экран во сколько раз планета
# Земля меньше или больше по объёму. Ответ округлите до трёх знаков после запятой

import math

R = float(input('Введите радиус случайной планеты: '))
V = 4/3 * math.pi * R ** 3
R_Earth = 10.8321 * 10**11

if R_Earth > R:
    print(f'Земпля больше случайной планеты в {round((R_Earth / R), 3)} раз.')
elif R_Earth < R:
    print(f'Земпля меньше случайной планеты в {round((R / R_Earth), 3)} раз.')
