seat = int(input("Введите ваше место: "))

if 1 <= seat <= 36:
    compartment = (seat-1) // 4+1
    print('Ваше купе: ', compartment)
else:
    print("Ошибка: в вагоне только 36 мест (номера 1-36) ")