line1 = set(map(int, input('Ввод 1: ').split()))
line2 = set(map(int, input('Ввод 2: ').split()))
line3 = set(map(int, input('Ввод 3: ').split()))

all_id = set(range(0, 11))

present_id = line1 | line2 | line3

ghosts = sorted(all_id - present_id)

print(f'Вывод: {ghosts}')