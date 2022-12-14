# Задача 6. Монетка
#
# Практиканту дали задание найти старую металлическую монетку по заданным координатам. Металлоискатель сканирует
# местность вокруг пользователя, и при обнаружении/отсутствии металла прибор отображает на экране соответствующее
# сообщение.
#
# Даны два действительных числа x и y. Напишите функцию, которая проверяет, принадлежит ли точка с координатами (x,
# y) заштрихованному квадрату (включая его границу). Если точка принадлежит квадрату, выведите сообщение «Монетка
# где-то рядом», в противном случае выведите сообщение «Монетки в области нет». На рисунке
# (https://go.skillbox.ru/media/files/share/1637681075044.png) сетка проведена с шагом 1.

def in_border(x, y):
    if (-1 <= x <= 1) and (-1 <= y <= 1):
        print('\nМонетка где-то рядом')
    else:
        print('\nМонетки в области нет')


x = float(input('Введите координаты точки по оси X: '))
y = float(input('Введите координаты точки по оси Y: '))
in_border(x, y)
