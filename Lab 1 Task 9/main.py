#Задача 9. Проверка IP адреса
ip = input("Введите IP: ")

parts = ip.split('.')

if len(parts) != 4:
    print("Неверный формат")
else:
    correct = True
    for part in parts:
        if not part.isdigit() or not (0 <= int(part) <= 255):
            correct = False
            break

    if correct:
        print("Корректный IP")
    else:
        print("Некорректный IP")