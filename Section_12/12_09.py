# Задача 9. Недоделка
#
# Вы пришли на работу в контору по разработке игр, целевая аудитория — дети и их родители. У прошлого программиста
# было задание сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них. Однако программист,
# на место которого вы пришли, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон
# проекта. Используя этот шаблон, реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
#
# Правила игры «Камень, ножницы, бумага»: программа запрашивает у пользователя строку и выводит, победил он или
# проиграл. Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
#
# Правила игры «Угадай число»: программа запрашивает у пользователя число до тех пор, пока он его не отгадает.
#
# def rock_paper_scissors():
#     # Здесь будет игра "Камень, ножницы, бумага"
#
# def guess_the_number():
#     # Здесь будет игра "Угадай число"
#
# def mainMenu():
#     # Здесь главное меню игры
#
# mainMenu():
#     pass
from random import randint


def rock_paper_scissors():
    user_answer = int(input('\nВыбранная игра: "Камень, ножницы, бумага"\n1 — камень\t2 — ножницы\t3 — '
                            'бумага\n\nВведите 0, чтобы выйти в меню.\n\nВвод: '))
    if user_answer == 0:
        print()
        mainMenu()
    elif user_answer == 1 or user_answer == 2 or user_answer == 3:
        AI_answer = randint(1, 3)
        if AI_answer == 1:
            print('\nКомпьютер выбрал камень (1)')
            if user_answer == 2:
                print('Вы выбрали ножницы (2)\n\nКамень бьет ножницы — победил компьютер!')
                rock_paper_scissors()
            elif user_answer == 3:
                print('Вы выбрали бумагу (3)\n\nБумага бьет камень — вы победили!')
                rock_paper_scissors()
            else:
                print('Вы выбрали камень (1)\n\nНичья!')
                rock_paper_scissors()
        elif AI_answer == 2:
            print('\nКомпьютер выбрал ножницы (2)')
            if user_answer == 3:
                print('Вы выбрали бумагу (3)\n\nНожницы бьют бумагу — победил компьютер!')
                rock_paper_scissors()
            elif user_answer == 1:
                print('Вы выбрали камень (1)\n\nКамень бьет ножницы — вы победили!')
                rock_paper_scissors()
            else:
                print('Вы выбрали ножницы (2)\n\nНичья!')
                rock_paper_scissors()
        else:
            print('\nКомпьютер выбрал бумагу (3)')
            if user_answer == 1:
                print('Вы выбрали камень (1)\n\nБумага бьет камень — победил компьютер!')
                rock_paper_scissors()
            elif user_answer == 2:
                print('Вы выбрали ножницы (2)\n\nНожницы бьют бумагу — вы победили!')
                rock_paper_scissors()
            else:
                print('Вы выбрали бумагу (3)\n\nНичья!')
                rock_paper_scissors()
    else:
        print('Неверный ввод. Попробуйте ещё раз.')
        rock_paper_scissors()


def guess_the_number():
    user_answer = int(input('\nВыбранная игра: "Угадай число"\nКомпьютер загадал число от 1 до 10. Попробуйте его '
                            'отгадать!\n\nВведите 1, чтобы начать.\nВведите 0, чтобы выйти в меню.\n\nВвод: '))
    if user_answer == 0:
        print()
        mainMenu()
    elif user_answer == 1:
        print('\nКомпьютер загадал число...\n')
        ai_answer = randint(1, 10)
        ask = -1
        try_count = 1
        while ask != ai_answer:
            ask = int(input('Введите число от 1 до 10.\nВвод: '))
            if ask < 1 or ask > 10:
                print('\nНеверный ввод. Попробуйте ещё раз.\n')
                continue
            if ask != ai_answer:
                try_count += 1
                print('\nНеверно. Попробуйте ещё раз.\n')
        print(f'\nВерно! Число {ai_answer} отгадано за {try_count} попыток!')
        guess_the_number()

    else:
        print('Неверный ввод. Попробуйте ещё раз.')
        guess_the_number()


def mainMenu():
    user_answer = int(input('Привет! Выбери игру:\n 1 — "Камень, ножницы, бумага"\t2 — "Угадай число"\n\nВвод: '))
    if user_answer == 1:
        rock_paper_scissors()
    elif user_answer == 2:
        guess_the_number()
    else:
        print('\nНеверный ввод. Попробуйте ещё раз.\n')
        mainMenu()


mainMenu()