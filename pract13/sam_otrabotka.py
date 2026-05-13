prices_str = '100 50 200 150 75 300'

print(prices_str.split())

ints = [int(x) for x in prices_str.split()]
print("Преобразование в числа",ints)

prices1 = ints.remove(max(ints))
print("Удалили самый дорогой товар",ints)

n = int(max(ints)*0.5)
ints.append(n)
print("Добавили новый товар со скидкой ",ints)

ints.sort()
print("Сортировка от меньшего к большему ",ints)

print("Среднее значение ",int((sum(ints))/(len(ints))))