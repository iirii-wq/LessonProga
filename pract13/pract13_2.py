numbers = []
flag = True
while flag:
    n = int(input("Введите натуральное число (0 чтобы закончить ввод): "))
    if n == 0:
        flag = False
    numbers.append(n)

del numbers[-1]
print(numbers)