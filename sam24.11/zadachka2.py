number_1 = float(input('Введите первое число: '))
operation = input('Введите операцию ( +, -, * или /):  ')
number_2 = float(input('Введите второе число: '))

match operation:
    case '+':
        summa = number_1 + number_2
        print(f'{number_1} + {number_2} = {summa}')
    case '-':
        vichet = number_1 - number_2
        print(f'{number_1} - {number_2} = {vichet}')
    case '/':
        delenie = number_1 / number_2
        print(f'{number_1} / {number_2} = {delenie}')
    case _:
        print('Неверная операция')