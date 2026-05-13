cry = set(input('Ввод (ЦРУ): ').split())
mi6 = set(input('Ввод (МИ-6): ').split())
kgb = set(input('Ввод (КГБ): ').split())

result = sorted((cry & mi6) - kgb, reverse=True)
print('Двойные агенты:', ''.join(result))
