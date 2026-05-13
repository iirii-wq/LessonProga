def solve(a, b, c):
    D = b ** 2 - 4 * a * c

    # Корни
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)

    if x1 <= x2:
        return x1, x2
    else:
        return x2, x1

print(solve(1, -4, -5))
print(solve(-2, 7, -5))
print(solve(1, 2, 1))