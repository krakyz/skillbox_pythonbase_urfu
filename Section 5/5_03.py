# Задача 3. Функция
# Учитель математики придумывает каждому своему ученику отдельные функции, которые нужно отобразить на графике и посчитать. А ещё этот учитель разбирается в программировании. Поэтому, чтобы не считать вручную все эти функции, он написал программу, которая делает всю работу за него.
# Напишите программу, которая получает от пользователя число X и вычисляет значение функции Y по следующей схеме:
# y= {x −12, x>0, 5,  x=0 x²,  x<0 
# Напомним, как это работает:
# для X > 0, Y = X − 12
# для X = 0,  Y = 5
# для X < 0, Y = X²
# Пример:
# Введите икс: 0
# Игрек равен 5
# Пример 2:
# Введите икс: −6
# Игрек равен 36

x = int(input('Введите X: '))

if x == 0:
    y = 5
elif x > 0:
    y = x - 12
else:
    y = x ** 2

print('Введен X:', x)
print('Y равен', y)
