import random

n = [[random.randint(-100, 100) for i in range (5)] for j in range(4)]

print("Исходный список:")
for row in n:
    print(row)

# фильтрую оставляя только положительные
plus = []
for row in n:
    new_row = []
    for num in row:
        if num > 0: # если число больше 0
            new_row.append(num)
    plus.append(new_row)

print("Только положительные (>0):")
for row in plus:
    print(row)