mileage = int(input('Введите пробег: '))
number = int(input('Введите сегодняшнее число: '))

mileage_digit_sum = mileage % 10 + mileage // 10 % 10 + mileage // 100

if mileage_digit_sum > number:
    print('Сброс.')
    mileage = 0
    print('Пробег:', mileage)
else:
    print('Сегодня не сломался')
    print('Пробег:', mileage)