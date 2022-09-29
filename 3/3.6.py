fisrt_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))

first_digits = fisrt_num % 100
second_digits = second_num % 100

print('Сумма:', first_digits + second_digits)