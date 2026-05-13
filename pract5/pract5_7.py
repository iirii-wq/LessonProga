print('Калькулятор поездки на такси')

def calculator_poezdki (rastoyanie, litr_na_km, cena_benz_za_litr):
    """Функция рассчитывает скольно понадобиться бензина и стоимость поездки"""

    kolvo_benz = rastoyanie * (litr_na_km / 100 )
    stoimost = kolvo_benz * cena_benz_za_litr
    return kolvo_benz, stoimost

rastoyanie = float(input('Введите расстояние которое потребуется преодолеть: '))
litr_na_km = float(input('Введите сколько литров на 100 км тратит машина: '))
cena_benz_za_litr = float(input('Введите цену бензина за 1 литр: '))

kolvo_benza, stoimosti = calculator_poezdki(rastoyanie, litr_na_km, cena_benz_za_litr)

print(f'Количество литров бензина: {kolvo_benza}')
print(f'Стоимость поездки: {stoimosti} рублей')