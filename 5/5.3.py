x = int(input('Введите X: '))

if x == 0:
    y = 5
elif x > 0:
    y = x - 12
else:
    y = x ** 2

print('Введен X:', x)
print('Y равен', y)
