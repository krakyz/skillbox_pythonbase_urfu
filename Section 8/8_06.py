# Задача 6. Письмо
#
# У нас есть квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги, которое не помещается
# в конверт. Напишите программу, которая подскажет, сколько раз нужно сложить письмо пополам, чтобы оно поместилось в
# конверт. Размеры письма вводятся с клавиатуры.

characteristics = int(input('Введите параметры письма: '))

counter = 0
while characteristics > 12:
    characteristics /= 2
    counter += 1
print(f'Чтобы письмо вошло в конверт, потребуется свернуть его пополам {counter} раз(а).')