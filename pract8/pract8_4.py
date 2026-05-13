print('Эта программа предсказывает размер популяции организмов')

m = int(input('Введите стартовое кол-во организмов: '))
p = int(input('Введите среднесуточное увеличение в процентах: '))
n = int(input('Введите кол-во дней для размножения: '))

factor = 1 + p /100 #вычисляем коэффицент увеличения (сложный процент)
sostoyanie_organizmov = m #текущее количество организмов

for day in range (1,n+1):
    print (f'День:{day}','размер популяции:', int(sostoyanie_organizmov))
    sostoyanie_organizmov = sostoyanie_organizmov * factor #увеличиваем популяцию для следующего дня
