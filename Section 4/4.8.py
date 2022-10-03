hours = int(input('Введите отработанные часы: '))
debt = int(input('Введите остаток по кредиту: '))
food = int(input('Введите траты на еду: '))

salary = (200 * hours) / (2**3) + hours

if salary >= (debt + food):
    print('Часов хватает, можно отдохнуть')
else:
    print('Часов не хватает. Придется работать!')