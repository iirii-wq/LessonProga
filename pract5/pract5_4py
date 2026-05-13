#S=pi*r**2
import math
def calculate_rectangle_area(width,height):
    """Используем формулу для расчета площади прямоугольника"""
    s_rectangle = width * height
    return s_rectangle
def calculate_circle_area(radius):
    """Используем формулу для расчета площади круга"""
    s_cirle = math.pi * radius**2
    return s_cirle
try:
    width, height = map(float, input('Введите ширину и высоту прямоугольника через пробел: ').split())
    s_rectangle = calculate_rectangle_area(width, height)
    print(f'Площадь прямоугольника:{s_rectangle}')
    radius = float(input('Введите радиус круга: '))
    s_circle = calculate_circle_area(width)
    print(f'Площадь круга: {s_circle:.2f}')
except ValueError:
    print('Ошибка! Пожалуйста, вводите числа.')



