chislo=int(input('Введите число: '))
tis=chislo//1000
print('тысячи',tis)
sotki=chislo//100%10
print('сотни', sotki)
desyatki=chislo//10%10
print('десятки',desyatki)
ed=chislo//1%10
print('единицы',ed)