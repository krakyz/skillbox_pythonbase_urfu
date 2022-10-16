# Задача 7. Наибольшая сумма цифр
#
# Пользователь вводит N чисел. Среди натуральных чисел, которые были введены, найдите наибольшее по сумме цифр.
# Выведите на экран это число и сумму его цифр.

max_sum = 0
while True:
    number = int(input('Введите число: '))
    current_sum = 0
    number_copy = number
    while number_copy != 0:
        current_sum += (number_copy % 10)
        number_copy //= 10
    if current_sum > max_sum:
        max_sum = current_sum
        max_number = number
    print(f'\nЧисло с наибольшей суммой: {max_number}\nНаибольшая сумма: {max_sum}\n')
