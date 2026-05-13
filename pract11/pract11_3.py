# Предварительно вычисляем все пятые степени от 1 до 150
pow5_to_num = {}
for i in range(1, 151):
    pow5_to_num[i ** 5] = i

max_e5 = 150 ** 5

found = False

for a in range(1, 151):
    a5 = a ** 5
    if a5 * 4 > max_e5:
        continue

    for b in range(a, 151):
        b5 = b ** 5
        if a5 + b5 * 3 > max_e5:
            break

        for c in range(b, 151):
            c5 = c ** 5
            if a5 + b5 + c5 * 2 > max_e5:
                break

            for d in range(c, 151):
                d5 = d ** 5
                sum5 = a5 + b5 + c5 + d5
                if sum5 > max_e5:
                    break

                if sum5 in pow5_to_num:
                    e = pow5_to_num[sum5]
                    print(f"Найдено: {a}^5 + {b}^5 + {c}^5 + {d}^5 = {e}^5")
                    print(f"Числа: a={a}, b={b}, c={c}, d={d}, e={e}")
                    print(f"Сумма a+b+c+d+e = {a + b + c + d + e}")
                    found = True

if not found:
    print("Решение не найдено в пределах до 150")