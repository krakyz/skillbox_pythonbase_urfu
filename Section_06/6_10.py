# Задача 10. Игра «Компьютер угадывает число»
#
# Поменяйте мальчика и компьютер из прошлой задачи местами. Теперь мальчик загадывает число между 1 и 100
# (включительно). Компьютер может спросить у мальчика: «Твоё число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер. Мальчик отвечает одним из трёх чисел: 1 — равно, 2 — больше,
# 3 — меньше.
#
# Напишите программу, которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.
#
# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.
#
# Подсказка:
# Используйте бинарный поиск, а не конкатенацию.

middle = answer = 0
low_range = 1
high_range = 100

while True:
    middle = int((low_range + high_range) / 2)
    print('Твоё число равно, меньше или больше, чем число ', middle, '?', sep='')
    ask = int(input('Введи ответ (1 — равно, 2 — больше, 3 — меньше): '))
    if ask == 1:
        print('Загаданное число —', middle)
        break
    if ask == 2:
        low_range = middle
    if ask == 3:
        high_range = middle
