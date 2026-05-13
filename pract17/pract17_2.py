def is_prime(num):
    # Функция для проверки, является ли число простым
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

print(is_prime(1))
print(is_prime(10))
print(is_prime(17))