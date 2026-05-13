balans = 1000
while True:
    print("1. Узнать баланс")
    print("2. Снять 100 руб")
    print("3. Положить 100 руб")
    print("4. Выход")
    command = int(input("Выберите что хотите сделать: "))
    if command == 1:
        print(f"Ваш текущий баланс: {balans}")
        continue
    elif command == 2:
        if balans >= 100:
            balans -= 100
            print("Снято 100 руб")

            continue
        else:
            print("Недостаточно средств")
    elif command == 3:
        balans += 100
        print("Добавлено 100")
        continue
    elif command == 4:
        print("До свидания")
        break
    else:
        print("Неверная команда")