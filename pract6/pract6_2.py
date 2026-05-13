number = int(input('Введите номер кармана: '))

if number == 0:
    print('Карман зеленый')
elif ((1 <=number <= 10 ) or ( 19 <= number <= 28)) and number % 2 == 0:
    print('Карман черный')
elif ((1 <=number <= 10 ) or (19 <= number <= 28)) and number % 2 == 1:
    print('Карман красный')
elif ((11 <=number <= 18) or (29 <= number <= 36)) and number % 2 == 0:
    print('Карман красный')
elif ((11 <=number <= 18 ) or (29 <= number <= 36)) and number % 2 == 1:
    print('карман черный')
else:
    print('Ошибка')
