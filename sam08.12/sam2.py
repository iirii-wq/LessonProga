composition = 1

while True:
    number = int(input("Введите число: "))

    if number < 0:
        break

    if number > 0:
        composition *= number

print(f"Результат произведения: {composition}")