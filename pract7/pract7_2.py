code = input('Введите статус вашего заказа (pending/processing/shipped/delivered/cancelled): ')

match code:
    case 'pending':
        russian_status = 'В ожидании'
        description = 'Заказ принят и ожидает подтверждения'
        emoji = '⌛'
        time_estimate = '1-2 часа'
    case 'processing':
        russian_status = 'В обработке'
        description = 'Заказ подтвержден и готовится к отправке'
        emoji = '📦'
        time_estimate = '2-24 часа'
    case 'shipped':
        russian_status = 'Отправлено'
        description = 'Заказ передан в службу доставки'
        emoji = '🚚'
        time_estimate = '1-7 дней'
    case 'delivered':
        russian_status = 'Доставлено'
        description = 'Заказ успешно доставлен получателю'
        emoji = '✅'
        time_estimate = 'Завершено'
    case 'cancelled':
        russian_status = 'Отменено'
        description = 'Заказ был отменен'
        emoji = '❌'
        time_estimate = 'Не определено'
    case _:
        russian_status = 'Неизвестный статус'
        description = 'Проверьте правильность введеного статуса'
        emoji = '❓'
        time_estimate = 'Не определено'
print('➖'*30)
print('             ✨ ИНФОРМАЦИЯ О СТАТУСЕ ЗАКАЗА ✨')
print('➖'*30)
print(f'            Статус: {russian_status} {emoji}')
print(f'            Описание: {description}')
print(f'            Примерное время ожидания: {time_estimate}')
print('➖'*30)