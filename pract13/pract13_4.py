ip = input("Введите ваш айпи адрес: ")

parts = ip.split('.')

if len(parts) == 4:
    print("YES")
else:
    print("NO")