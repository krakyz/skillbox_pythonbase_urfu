# Задача 9. В обратном порядке
# Реализуйте программу, которая получает на вход четырёхзначное число и выводит его на экран в обратном порядке. Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания. Однако можно использовать сколько угодно переменных. Пример ввода: 1234. Пример вывода: 4321.

num = int(input('Введите четырехзначное число: '))
print('Каждая цифра числа в обратном порядке:', num % 10, num // 10 % 10, num // 100 % 10, num // 1000)
