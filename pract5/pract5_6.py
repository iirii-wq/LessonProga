import math

def calculate_distance(x1, y1, x2, y2):
    """Используем формулу для нахождения дистанции"""
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_triangle_area(a, b, c):
    """Используем формулу для нахождения полупериметра и формулу Герона"""
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area

# ввод координат для стороны AB
x1, y1, x2, y2 = map(float, input("Координаты А и В (x1 y1 x2 y2): ").split())
side1 = calculate_distance(x1, y1, x2, y2)

# ввод координат для стороны BC
x3, y3, x4, y4 = map(float, input("Координаты B и C (x3 y3 x4 y4): ").split())
side2 = calculate_distance(x3, y3, x4, y4)

# ввод координат для стороны CA
x5, y5, x6, y6 = map(float, input("Координаты C и A (x5 y5 x6 y6): ").split())
side3 = calculate_distance(x5, y5, x6, y6)

print(f"Длина сторон: AB-{side1:.2f}, BC-{side2:.2f}, CA-{side3:.2f}")

area = calculate_triangle_area(side1, side2, side3)
print(f"Площадь треугольника по формуле Герона: {area:.2f}")
