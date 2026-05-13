log1 = set(input('Ввод 1: ').split())
log2 = set(input('Ввод 2: ').split())
log3 = set(input('Ввод 3: ').split())

result = sorted((log1 | log2 | log3) - (log1 & log2 & log3))

print('Результат:', ''.join(result))