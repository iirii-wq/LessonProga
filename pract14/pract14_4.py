import random

n = [[random.randint(1, 100) for i in range (5)] for j in range(4)]

print("Исходный список:")
for row in n:
    print(row)

search_num = int(input('Введите число которое нужно найти: '))

found = []
for i in range(len(n)):
    for j in range(len(n[i])):
        if n[i][j] == search_num:
            found.append((i,j))

print(f'Число {search_num}:')
if found:
    for pos in found:
        print(f'Найдено на позиции [{pos[0]}][{pos[1]}]')
else:
    print('Не найдено')