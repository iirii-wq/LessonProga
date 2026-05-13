b5000 = 5000
b2000 = 2000
b1000 = 1000
b500 = 500
b100 = 100
b50 = 50
try:
    money = int(input('Введите число которое хотить снять, кратное 100: '))
    pyat_ts = money//b5000
    print(f'Кол-во купюр по 5 тыс.: {pyat_ts}')
    dve_ts = (money % b5000) // b2000
    print(f'Кол-во купюр по 2 тыс.: {dve_ts}')
    odna_ts = (money % b5000 % b2000) // b1000
    print(f'Кол-во купюр по 1 тыс.: {odna_ts}')
    pyatsot = (money % b5000 % b2000 % b1000) // b500
    print(f'Кол-во купюр по 500 р.: {pyatsot}')
    sto = (money % b5000 % b2000 % b1000 % b500) // b100
    print(f'Кол-во купюр по 100 р.: {sto}')
    pyat_desyat = (money % b5000 % b2000 % b1000 % b500 % b100 )//b50
    print(f'Кол-во купюр по 50 р.: {pyat_desyat}')
except ValueError:
    print('Ошибка! Пожалуйста, вводите числа.')




