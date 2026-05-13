n1 = int(input("Введите первое число: "))

while True:
    n2 = int(input("Введите второе число: "))
    if n2 > n1:
        break
    print("Ошибка")

while True:
    n3 = int(input("Введите третье число: "))
    if n3 > n2:
        break
    print("Ошибка")

print(f'Последовательность принята: {n1},{n2},{n3}')