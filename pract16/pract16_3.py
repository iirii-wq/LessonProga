server_a = set(input('Ввод (Сервер А): ').split())
server_b = set(input('Ввод (Сервер В): ').split())

common = sorted(server_a & server_b)
lost = sorted(server_a - server_b)

print('Общие:', ''.join(common))
print('Потерянные:', ''.join(lost))