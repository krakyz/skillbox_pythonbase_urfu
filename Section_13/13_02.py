# Задача 2. Функция максимума
#
# Юра пишет различные полезные функции для Питона, чтобы остальным программистам стало проще работать. Он захотел
# написать функцию, которая будет находить максимум из перечисленных чисел. Функция для нахождения максимума из двух
# чисел у него уже есть. Юра задумался: может быть, её можно как-то использовать для нахождения максимума уже от трёх
# чисел?
#
# Помогите написать Юре функцию, которая находит максимум из трёх чисел. Для этого используйте только функцию
# нахождения максимума из двух чисел.

def max_of_threee(first_number, second_number, third_number):
    max_num = max(max(first_number, second_number), third_number)
    return max_num


a = float(input('Введите первое число: '))
b = float(input('Введите тертье число: '))
c = float(input('Введите второе число: '))
print(f'\nСамое большое число — {max_of_threee(a, b, c)}')