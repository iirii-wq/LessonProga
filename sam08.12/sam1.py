attempt = 1

while True:
    password = input("Введите пароль: ")
    if password == "admin":
        print("Доступ разрешен")
        break

    if attempt == 3:
        print("Попытки закончились")
        print("Вход заблокирован")
        break
    attempt += 1