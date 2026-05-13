def is_valid_triangle (side1, side2, side3):
    if (side1+side2>side3) and (side1+side3>side2) and (side2+side3>side1):
        return True
    else:
        return False
print(is_valid_triangle(2,2,2))
print(is_valid_triangle(2,3,10))
print(is_valid_triangle(3,4,5))