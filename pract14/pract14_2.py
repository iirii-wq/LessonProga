import random

n = [[random.randint(0, 100) for i in range (5)] for j in range(4)]

print(f'Список: {n}')

# сумма строк
row_sum = []
for row in n:
    row_sum.append(sum(row))

print(f'Суммы строк: {row_sum}')
for i, s in enumerate(row_sum):
    print(f'Строка {i} : {s}')

# общая сумма
total = sum (row_sum)
print(f'Общая сумма: {total}')

# строка с макс суммой
max_id = row_sum.index(max(row_sum))
print(f'Строка с макс суммой: {max_id}')
print(F'Сумма: {row_sum[max_id]}')
print(f'Элементы: {n[max_id]}')