def is_password_good(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False

    # Проверка символов
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    # Пароль надёжный если выполнены все три условия
    if has_upper and has_lower and has_digit:
        return True
    else:
        return False

print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))