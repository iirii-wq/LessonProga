marks = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5]

fives = 0
twos = 0

for mark in marks:
    if mark == 5:
        fives += 1
    elif mark == 2:
        twos += 1

print(f"Список оценок: {marks}")
print(f"Количество пятерок: {fives}")
print(f"Количество двоек: {twos}")