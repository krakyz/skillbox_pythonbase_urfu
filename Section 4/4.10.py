first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))
third_num = int(input('Введите третье число: '))

if first_num > second_num and first_num > third_num:
    print('Максимальное число - первое:', first_num)
elif second_num > first_num and second_num > third_num:
    print('Максимальное число - второе:', second_num)
else:
    print('Максимальное число - третье:', third_num)
