# Задача 5. Текстовый редактор
#
# Мы продолжаем разрабатывать новый текстовый редактор, и в этот раз нам поручили написать для него код,
# который считает количество любой буквы и любой цифры в тексте (а не только буквы Ы, как раньше).
#
# Напишите функцию count_letters, которая принимает на вход текст и подсчитывает, какое в нём количество цифр K и
# букв N. Функция должна вывести на экран информацию о найденных буквах и цифрах в определённом формате.
#
# Пример:
#
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищем? л
# Количество цифр 0: 2
# Количество букв л: 1


def count_letters(text, K, N):
    print(f'Количество цифр {K}: {text.count(K)}')
    print(f'Количество букв {N}: {text.count(N)}')


text = input('Введите текст: ')
K = input('Введите цифру для поиска: ')
N = input('Введите букву для поиска: ')

count_letters(text, K, N)
