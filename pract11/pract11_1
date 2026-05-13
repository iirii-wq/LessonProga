#n = 28
#k = 30
#m = 31

#for n in range(1, 3):
#    k = 7 - 3*n
#    m = 5 + 2*n
#    print(n, k, m)
print("Все тройки натуральных чисел (n, k, m):")

found_solutions = False

for n in range(1,13):
    for k in range(1,13):
        m = 12 - n - k
        if m < 1: # m должно быть натуральным
            continue
        if 28*n+30*k+31*m==365: # проверка уравнения
            print(f"n = {n}, k = {k}, m = {m}")
            found_solutions = True

if not found_solutions:
    print("Решений нет")
