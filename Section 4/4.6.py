player_res = int(input('Кубик Кости: '))
owner_res = int(input('Кубик владельца: '))

if player_res >= owner_res:
    print('Разность: ', player_res - owner_res)
    print('Костя платит')
else:
    print('Сумма:', player_res + owner_res)
    print('Владелец платит')
print('Игра окончена')
