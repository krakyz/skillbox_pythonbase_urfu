# Задача 8. Колонтитул
# Что нужно сделать
#
# Нам нужно написать программу для печати важных объявлений. Сверху объявления должен располагаться вот такой
# колонтитул: ~~~~~~~!!!!!!!~~~~~~~
#
# Восклицательные знаки всегда располагаются по центру строки, причём в зависимости от важности объявления количество
# восклицательных знаков может быть разным. Напишите программу, которая спрашивает у пользователя сначала общую длину
# колонтитула в символах, потом желаемое количество восклицательных знаков, после чего выводит на экран готовую строку.

total_lenght = int(input('Введите общую длину колонтитула: '))
exclamation_marks = int(input('Введите кол-во восклицательных знаков: '))

tildasQ = int((total_lenght - exclamation_marks) / 2)

print(('~' * tildasQ) + ('!' * exclamation_marks) + ('~' * tildasQ))
