price = int(input("Введите цену: "))

# Списки для хранения монет
coins_25 = 0
coins_10 = 0
coins_5 = 0
coins_1 = 0

while price > 0:
    if price >= 25:
        price -= 25
        coins_25 += 1
    elif price >= 10:
        price -= 10
        coins_10 += 1
    elif price >= 5:
        price -= 5
        coins_5 += 1
    else: # price >= 1
        price -= 1
        coins_1 += 1

# Вычисляем общее количество монет
total_coins = coins_25 + coins_10 + coins_5 + coins_1

# Выводим результат
print(f"Общее количество монет: {total_coins}")
