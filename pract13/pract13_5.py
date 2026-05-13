numbers = input("Введите числа через пробел: ")

ints = [int(x) for x in numbers.split()]
count = 0

for i in range(len(ints)):
    for j  in range (i + 1,len(ints)):
        if ints[i] == ints[j] :
            count += 1

print("Всего пар: ",count)