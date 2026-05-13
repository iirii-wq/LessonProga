print('Контроль доступа')

allowed = {"10","20","30"}
incoming = ["20","40","10","50"]

for id_str in incoming:
    if id_str in allowed:
        print('OK')
    else:
        print('ADDED')