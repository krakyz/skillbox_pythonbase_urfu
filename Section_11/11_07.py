# Задача 7. Ход конём
#
# В рамках разработки шахматного ИИ стоит новая задача. По заданным вещественным координатам коня и второй точки
# программа должна определить может ли конь ходить в эту точку. Используйте как можно меньше конструкций if и
# логических операторов. Обеспечьте контроль ввода.
#
# Пример:
# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.

import math

x1, y1 = float(input('Введите местоположение коня: \n')), float(input())
x2, y2 = float(input('Введите местоположение точки на доске: \n')), float(input())

print(f'Конь в клетке {math.floor(x1 * 10), math.floor(y1 * 10)}. Точка в клетке {math.floor(x2 * 10), math.floor(y2 * 10)}')
if (int(x1 * 10) - int(x2 * 10)) * (int(y1 * 10) - int(y2 * 10)) in [-2, 2]:
    print('Да, конь может ходить в эту точку.')
else:
    print('Нет, конь не может ходить в эту точку.')


