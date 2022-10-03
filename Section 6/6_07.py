# Задача 7. Обычный день на работе
#
# Максим программирует целый день на работе и вечером идёт домой. Каждый час начальство кидает ему несколько задач,
# которые нужно решить до следующего рабочего часа. Вдобавок каждый час Максиму звонит супруга. Он знает, что если он
# возьмёт трубку, то жена попросит зайти вечером в магазин.
#
# Напишите программу, в которой считается, сколько задач выполнил Максим за день (8 часов). Если он хоть раз взял
# трубку, то в конце дополнительно выводите сообщение: «Нужно зайти в магазин».
#
# Пример:
#
# Начался 8-часовой рабочий день
# 1-й час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 2-й час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 3-й час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 4-й час
# Сколько задач решит Максим? 4
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 1
# 5-й час
# Сколько задач решит Максим? 5
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 6-й час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 7-й час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 1
# 8-й час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
#
# Рабочий день закончился. Всего выполнено задач: 21
#
# Нужно зайти в магазин.

hours = 1
tasks = 0
while hours <= 8:
    print(hours, '-й час', sep='')
    tasks += int(input('Сколько задач решит Максим? '))
    phone = input('Звонит жена. Взять трубку? (1 — да, 0 — нет): ')
    hours += 1
print('Рабочий день закончился. Всего выполнено задач:', tasks)

if phone == 1:
    print('Нужно зайти в магазин.')
