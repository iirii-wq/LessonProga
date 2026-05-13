count = 0
alex = False
name = input('Введите имя: ')
while name != 'Левон':
    if name == 'Александра':
        alex = True
    elif alex:
        count += 1
    name = input('Введите имя: ')

print(f'Человек в очереди между Алексаднрой и Левоном: {count}')