def calculate_bmi(massa_tela, rost):
    """Рассчитывает ИМТ и возвращает классификацию"""
    bmi = massa_tela/rost**2
    return bmi

def get_imt_category(bmi):
    """Определяет категорию ИМТ"""
    if bmi < 16:
        return "выраженный дефицит массы тела"
    elif 16 <= bmi < 18.5:
        return "недостаточная масса тела"
    elif 18.5 <= bmi < 25:
        return "нормальная масса тела"
    elif 25 <= bmi < 30:
        return "избыточная масса тела"
try:
    massa_tela, rost = map(float, input('Введите ваш вес в кг и рост в метрах: ').split())
    bmi = calculate_bmi(massa_tela, rost)
    category = get_imt_category(bmi)

    print(f'Ваш индекс массы тела: {bmi:.1f} - {category}')
except ValueError:
    print('Ошибка! Пожалуйста, вводите числа.')
