A = int(input('Введите целое положительное число A: '))
B = int(input('Введите целое положительное число B: '))

if A > B:
    A, B = B, A

#определяем первое четное и нечетное число в диапазоне
first_even = A if A % 2 == 0 else A + 1
first_odd = A if A % 2 != 0 else A + 1

#определяем кол-во четных и нечетных чисел в диапазоне
if first_even > B:
    count_even = 0
else:
    count_even = (B - first_even) // 2 + 1

if first_odd > B:
    count_odd = 0
else:
    count_odd = (B - first_odd) // 2 + 1

#суммы арифм. прогрессий
sum_even = (first_even + (first_even + 2 * (count_even - 1))) * count_even // 2 if count_even > 0 else 0
sum_odd = (first_odd + (first_odd + 2 * (count_odd - 1))) * count_odd // 2 if count_odd > 0 else 0

#разность между суммой четных и суммой нечетных
result = sum_even - sum_odd
print(f'Разность между суммой четных и нечетных чисел от А до В: {result}')