import random

print('Программа загадала число попробуй его угадать!(У тебя 3 попытки)')

#программа загадывает число от 1 до 10
secret = random.randint(1, 10)
attempts = 3

for i in range(1, attempts + 1):
    guess = int(input('Введите число: '))  # Считываем попытку пользователя

    if guess == secret:
        print("Угадали!")
        break  #завершаем игру
    else:
        print("Неверно", end="")
        if guess < secret:
            print(", нужно больше")
        else:
            print(", нужно меньше")

    #если это была последняя попытка и не угадали
    if i == attempts:
        print(f"Загаданное число: {secret}")