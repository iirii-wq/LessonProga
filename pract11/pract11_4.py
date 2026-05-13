n = int(input("Введите натуральное число: "))

count_3 = 0
count_last_digit = 0
count_even = 0
sum_more_5 = 0
product_more_7 = 1
count_0_or_5 = 0

if n == 0:
    count_last_digit = 1
    count_even = 1
    count_0_or_5 = 1
else:
    last_digit = n % 10 #Нахождение последней цифры
    temp = n
    count_gt_seven = 0 #Счетчик цифр больших 7
    while temp > 0:
        digit = temp % 10 # Получаем последнюю цифру
        # Кол-во цифр 3
        if digit == 3:
            count_3 += 1
        # Кол-во раз встречается последняя цифра
        if digit == last_digit:
            count_last_digit += 1
        # Кол-во четных чисел
        if digit % 2 == 0:
            count_even += 1
        # Сумма чисел больших пяти
        if digit > 5:
            sum_more_5 += digit
        # Произведение цифр больших семи
        if digit > 7:
            product_more_7 *= digit
            count_gt_seven += 1
        # Кол-во раз встречаются цифры 0 и 5
        if digit == 0 or digit == 5:
            count_0_or_5 += 1
        # Убираем последнюю цифру
        temp //= 10

    if count_gt_seven == 0:
        product_more_7 = 1

print(f"Кол-во цифр 3: {count_3}")
print(f"Кол-во раз встречается последняя цифра: {count_last_digit}")
print(f"Кол-во четных цифр: {count_even}")
print(f"Сумма цифр больших 5: {sum_more_5}")
print(f"Произведение цифр больших 7: {product_more_7}")
print(f"Кол-во раз встречаются цифры 0 и 5: {count_0_or_5}")