# Задача 8. Замечательные числа
#
# Напишите программу, которая находит и выводит все двузначные числа, которые равны утроенному произведению своих
# цифр. К таким относятся, например, 15 и 24.

for number in range(10, 100):
    first_digit = number // 10 % 10
    second_digit = number % 10
    if (first_digit * second_digit) * 3 == number:
        print(number)
