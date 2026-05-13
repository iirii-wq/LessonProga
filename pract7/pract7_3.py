cofe_price = 120
tea_price = 80
juise_price = 100
water_price = 50
lemonade_price = 90

#скидки
discount = {
    "WELCOME_10": 10,
    "STUDENT_15": 15,
    "VIP_20": 20
}

print('➖'*30)
print('                 ДОБРО ПОЖАЛОВАТЬ В КАФЕ')
print('➖'*30)
print('📌 НАШЕ МЕНЮ:')
print('1. ☕ Кофе - 120 рублей')
print('2. 🍵 Чай - 80 рублей')
print('3. 🧃 Сок - 100 рублей')
print('4. 💧 Вода - 50 рублей')
print('5. 🍹 Лимонад - 90 рублей')
print('➖'*30)

user_drink = input('Выберите напиток (номер или словом): ')

match user_drink:
    case '1' |'кофе' | 'Кофе' :
        drink_name = '☕ Кофе'
        price = cofe_price
    case '2' |'чай' | 'Чай' :
        drink_name = '🍵 Чай'
        price = tea_price
    case '3' |'сок' | 'Сок':
        drink_name = '🧃 Сок'
        price = juise_price
    case '4' |'вода' | 'Вода':
        drink_name = '💧 Вода'
        price = water_price
    case '5' |'лимонад' | 'лимонад':
         drink_name = '🍹 Лимонад'
         price = lemonade_price
    case _:
        print('❌ Ошибка! Напиток не найден в меню.')
try:
    quantity = int(input("Введите количество порций: "))
    if quantity <= 0:
        print("❌ Ошибка! Количество должно быть положительным числом.")
except ValueError:
    print("❌ Ошибка:! Введите целое число.")

discount_user = input('Введите промокод (если нет - нажмите Enter): ')
discount_percent = 0

if discount_user:
    match discount_user:
        case "WELCOME_10":
            discount_percent = discount["WELCOME_10"]
        case "STUDENT_15":
            discount_percent = discount["STUDENT_15"]
        case "VIP_20":
            discount_percent = discount["VIP_20"]
        case _:
            print("❗ Код скидки недействителен")

total = quantity * price
discount_amount = total * discount_percent // 100
final_amount = total - discount_amount

if quantity == 1:
    portion = 'порция'
elif 2 <= quantity <= 4:
    portion = 'порции'
else:
    portion = 'порций'

print('➖'*30)
print('ВАШ ЗАКАЗ:')
print('➖'*30)
print(f'Напиток: {drink_name}')
print(f'Цена за порцию: {price} рублей')
print(f'Количество: {quantity} {portion}')
print(f'Сумма: {total} рублей')

if discount_percent > 0:
    print(f'Скидка {discount_percent}%: {discount_amount} рублей')
else:
    print('Скидка: не применена')

print('➖'*30)
print(f'Итого к оплате: {final_amount} рублей')
print('➖'*30)
print('✨ Спасибо за заказ! Приятного аппетита! ✨')
print('➖'*30)