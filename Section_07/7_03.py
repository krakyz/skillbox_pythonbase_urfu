# Задача 3. Посчитай чужую зарплату...
#
# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании и, чтобы облегчить себе
# жизнь, обратилась к программисту.
#
# Напишите программу, которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев и выводит на
# экран среднюю зарплату за год.

avg_wage = 0
for month in range(1, 13):
    wage = int(input(f'Введите зарпалату за  {month} месяц: '))
    avg_wage += wage / 12
print('Средняя зарплата за год составляет', round(avg_wage), 'руб.')
