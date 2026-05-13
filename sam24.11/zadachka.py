print('=== Определение сезона ====')
month = int(input('Введите номер месяца: '))

match month:
    case 1 | 2 | 12:
        emoji = '❄️'
        print(f'Зима {emoji}')
    case 3| 4| 5:
        emoji = '🌸'
        print(f'Весна {emoji}')
    case 6| 7| 8:
        emoji = '☀️'
        print(f'Лето {emoji}')
    case 9| 10 | 11 :
        emoji = '🍁'
        print(f'Осень {emoji}')
    case _:
        print('Некорректный ввод 👺👺👺')