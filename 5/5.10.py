enter_hour = int(input('Введите время от 0 до 23 часов: '))

if enter_hour > 23 or enter_hour < 0:
    print('Ошибка: введено некорректное время.')

if 8 <= enter_hour < 22:
    if (10 <= enter_hour < 12 or 18 <= enter_hour < 20) or (enter_hour == 14):
        print('Посылку получить нельзя.')
    else:
        print('Можно получить посылку.')
else:
    print('Посылку получить нельзя.')
