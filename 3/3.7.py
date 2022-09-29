v = int(input('Введите скорость (км/ч): '))
t = int(input('Введите время (ч): '))
road_s = 115
total_s = v * t
circle_s = total_s % road_s

print('Ответ:', circle_s)
print('Пройденное расстояние составит', total_s, 'км, значит Вася будет на отметке', circle_s, 'км.')
