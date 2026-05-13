print("Программа выводит простые числа в заданном диапазоне")
a = int(input("Введите число: "))
b = int(input("Введите число: "))

for num in range(a, b + 1):
    if num < 2:
        continue
    is_prime = True
    for i in range(2,int(num ** 0.5) + 1):
        # Сперва возводим число в степень 0.5, округляем его с помощью int и добавляем 1
        if num % i == 0: #Проверка на простое число, если num делится на i без остатка то num не считается простым числом
            is_prime = False
            break
    if is_prime:
        print(num)

