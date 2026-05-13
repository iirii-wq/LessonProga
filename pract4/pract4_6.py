import math
x=float(input("Введите действительное число "))
radian= math.radians(x)
formula=math.sin(radian)+math.cos(radian)+math.tan(radian)**2
print('Значени тригонометрического выражения: ',formula)