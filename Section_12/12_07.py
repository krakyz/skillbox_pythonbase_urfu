# Задача 7. Опять?
#
# Вы снова встретились со своим старым другом, который был безмерно благодарен вам за то, что вы помогли ему сдать
# задачу тому преподавателю. Вот только друг всё равно выглядел довольно грустным. Когда вы спросили, в чём дело,
# друг взорвался эмоциями и рассказал, что теперь препод попросил написать функцию нахождения минимального числа без
# использования условного оператора и циклов. Конечно же, вы решили снова помочь бедняге. Напишите для него такую
# программу.

def minimum_number(first_number, second_number):
    print(f'\nМинимальное число равно {min(first_num, second_num)}')


first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))

minimum_number(first_num, second_num)
