# Задача 2. Я стал новым пиратом!
#
# Старому капитану необходимо пополнить команду. Но попадут на его корабль только достойные! Он отобрал 10 человек и
# те, кто из них крикнет слово “Карамба”, попадут на борт.
#
# Пользователь вводит 10 слов. Напишите программу, которая определяет, сколько из них совпадают со словом «Карамба».

newPiratesCount = 0
for recruit in range(10):
    text = input('Введите выкрикнутое слово: ')
    if (text == 'Карамба') or (text == 'карамба'):
        newPiratesCount += 1
print(f'Совпало {newPiratesCount} слов.')