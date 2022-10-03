# Игра в кубики
# Костя играет в азартную игру с кубиками с владельцем заведения. Правда, с довольно интересными правилами: если у Кости на кубике выпадет столько же или больше, чем у владельца, то Костя задолжает разность в тысячах долларов. Однако если выпадет меньше, то Косте выплатят столько тысяч долларов, сколько будет сумма очков на кубиках.
# Напишите программу. На вход в программу подаётся два числа. Если первое число больше либо равно второму, нужно вывести на экран их разность и отдельной строкой фразу: «Костя платит». В противном случае вывести их сумму и отдельной строкой — фразу: «Владелец платит». Также последней строкой в результате нужно вывести на экран фразу: «Игра окончена».

player_res = int(input('Кубик Кости: '))
owner_res = int(input('Кубик владельца: '))

if player_res >= owner_res:
    print('Разность: ', player_res - owner_res)
    print('Костя платит')
else:
    print('Сумма:', player_res + owner_res)
    print('Владелец платит')
print('Игра окончена')