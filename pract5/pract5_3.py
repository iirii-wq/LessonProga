def convert_usd_to_rub(amount_usd):
    """Конвертирует доллары в рубли"""
    converted_usd = amount_usd * kurs_usd
    return converted_usd
try:
    amount_usd = float(input('Введите вашу сумму в долларх: '))
    kurs_usd = float(input('Введите курс доллара: '))
    converted_usd = convert_usd_to_rub(amount_usd)
    print(f'Ваша сумма в рублях: {converted_usd}')
except ValueError:
    print('Ошибка! Пожалуйста, вводите числа')



