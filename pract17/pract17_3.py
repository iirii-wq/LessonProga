def is_prime(num):
    # Функция для проверки, является ли число простым
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def get_next_prime(num):
    # Начинаем проверку со следующего числа после num
    next_number = num + 1

    # Ищем первое простое число
    while True:
        if is_prime(next_number):
            return next_number
        next_number += 1

print(get_next_prime(6))
print(get_next_prime(7))
print(get_next_prime(14))