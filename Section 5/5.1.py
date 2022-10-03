exp = int(input('Введите количество опыта: '))
level = 1

if 1000 <= exp < 2500:
    level = 2
elif 2500 <= exp < 5000:
    level = 3
elif exp >= 5000:
    level = 4

print('Ваш уровень:', level)
