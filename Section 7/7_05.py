# Задача 5. Факториал
#
# Мы всё ближе и ближе подбираемся к серьёзной математике. Одна из классических задач — задача на нахождение
# факториала числа. И в будущем мы с ней ещё встретимся.
#
# Дано натуральное число n. Напишите программу, которая находит n! (n-факториал).
# Запись n! означает следующее:
# n! = 1 * 2 * 3 * 4 * 5 * … * n
#
# Пример:
#
# Введите число: 5
# Факториал числа 5 равен 120

number = int(input('Введите натуральное число: '))
result = 1
for number in range(1, number + 1):
    result *= number
print(f'Факториал числа {number} равен {result}')