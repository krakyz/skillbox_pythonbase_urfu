# Задача 6. Проверяем бухгалтера
# Невнимательный бухгалтер Антон складывает числа быстро, но иногда забывает о двух последних разрядах. Напишите программу, которая бы складывала только два последних разряда. 
# Реализуйте программу, которая запрашивает два числа у пользователя. После этого у каждого числа возьмите две последние цифры. Получившиеся два числа сложите и выведите на экран. Пример:
# Введите первое число: 111
# Введите второе число: 904
# Сумма: 15

fisrt_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))

first_digits = fisrt_num % 100
second_digits = second_num % 100

print('Сумма:', first_digits + second_digits)
