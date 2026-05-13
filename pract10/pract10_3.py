max_n = None

while True:
    n = int(input("Введите натуральное число (0 для остановки): "))
    if n == 0:
        break

    if max_n is None or n > max_n:
        max_n = n

if max_n is not None:
    print(f"Самое большое число: {max_n}")
else:
    print("Вы не ввели ни одного натурального числа")
