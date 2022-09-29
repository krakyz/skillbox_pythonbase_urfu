first_q = input('Доход за 1 квартал: ')
second_q = input('Доход за 2 квартал: ')
penult_q = input('Доход за предпоследний квартал: ')
last_q = input('Доход за последний квартал: ')

first_two_sum = int(first_q) + int(second_q)
last_two_sum = int(penult_q) + int(last_q)

print(first_two_sum / last_two_sum)