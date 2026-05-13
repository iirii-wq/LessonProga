word = input("Введите слово: ")

list1 = []
list1 += word
print(list1)
list2 = (list1[::-1])

if list1 == list2:
    print(list2)
    print("Это палиндром!")
else:
    print(list2)
    print("Не палиндром.")
