numbers = [8, 9, 10, 11]
print("Исходный список:", numbers)

numbers[1]= 17
print("После замекны второго элемента на 17: ",numbers)

numbers.extend([4,5,6])
print("После добавления 4, 5, 6 в конец: ",numbers)

numbers.pop(0)
print("После удаления первого элемента: ",numbers)

numbers = numbers * 2
print("После удвоения списка: ",numbers)

numbers.insert(3, 25)
print("После вставки 25 по индексу 3: ",numbers)

print("Итоговый список: ", numbers)