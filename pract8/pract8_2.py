print('Введите 10 целых чисел:')


all_even = True
for i in range (10):
    num = int(input(f'Число {i+1}: '))
    if num % 2 != 0:
        all_even = False

if all_even:
    print('YES')
else:
    print('NO')