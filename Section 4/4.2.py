language = int(input('Введите количество баллов по русскому языку: '))
math = int(input('Введите количество баллов по математике: '))
informatics = math = int(input('Введите количество баллов по информатике: '))

if language + math + informatics >= 270:
    print('Поздравляю, ты поступил на бюджет!')
else:
    print('К сожалению, ты не прошёл на бюджет.')