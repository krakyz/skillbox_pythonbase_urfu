first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first >= second and first >= third:
    print('Максимальное число:', first)
elif second >= first and second >= third:
    print('Максимальное число:', second)
elif third >= first and third >= second:
    print('Максимальное число:', third)
