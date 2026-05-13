price_all = 0

while True:
    price_product = int(input("Введите цену товара: "))
    if price_product == 0:
        break

    if price_product < 0:
        print("Ошибка цены")
        continue

    price_all += price_product

if price_all > 1000:
    skidka10 = price_all-(price_all * 0.1)
    print(f"Сумма к оплате: {skidka10}")
else:
    print(f"Сумма к оплате: {price_all}")