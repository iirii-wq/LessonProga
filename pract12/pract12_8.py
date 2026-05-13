import random

# Создаем список из 5 случайных чисел
numbers = [random.randint(1, 100) for _ in range(5)]
print(f"Исходный список: {numbers}")

# Находим индекс минимального элемента
min_index = numbers.index(min(numbers))

# Меняем местами первый элемент с минимальным
numbers[0], numbers[min_index] = numbers[min_index], numbers[0]

print(f"Список после обмена: {numbers}")