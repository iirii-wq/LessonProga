numbers = [10, 20, 30, 40, 50]
n = int(input("Введите число: "))

found = False
for i in range(len(numbers)):
    if n == numbers[i]:
        print(f"Число {n} найдено")
        found = True
        break

if not found:
    print('Нет такого числа')