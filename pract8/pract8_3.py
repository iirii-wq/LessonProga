x = int(input('Введите натуральное число: '))

total = 0

for i in range(1, x+1):
    if i % 2 ==1:
        total +=i
    else:
        total -= i

print(f'Значение суммы: {total}')