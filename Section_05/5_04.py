# Задача 4. Поступление
# В университете на факультет кибернетики очень серьёзный конкурс — поступают только сильнейшие, первые десять человек из списка. Потом среди поступивших определяется, кто будет получать стипендию. Для стипендии общий балл при поступлении должен быть не менее 290.
# Напишите программу, которая получает на вход место студента в списке и его балл, а затем выводит соответствующие сообщения о поступлении и получении стипендии.
# Пример 1:
# Введите место в списке поступающих: 3
# Введите количество баллов за экзамены: 295
# Поздравляем, вы поступили!
# Бонусом вам будет начисляться стипендия.
# Пример 2:
# Введите место в списке поступающих: 3
# Введите количество баллов за экзамены: 270
# Поздравляем, вы поступили!
# Но вам не хватило баллов для стипендии.
# Пример 3:
# Введите место в списке поступающих: 11
# К сожалению, вы не поступили.

place = int(input('Введите место в списке поступающих: '))

if place > 10:
    print('К сожалению, вы не поступили')
else:
    points = int(input('Введите количество баллов за экзамены: '))
    print('Поздравляем, вы поступили!')
    if points >= 290:
        print('Бонусом вам будет начисляться стипендия.')
    else:
        print('Но вам не хватило баллов для стипендии.')
