first_price = int(input('Введите стоимость первого товара: '))
second_price = int(input('Введите стоимость второго товара: '))
third_price = int(input('Введите стоимость третьего товара: '))
total = first_price + second_price + third_price

if total > 10000:
    print(total - (total * 10 / 100))
else:
    print('Итоговая цена не превышает 10 000')