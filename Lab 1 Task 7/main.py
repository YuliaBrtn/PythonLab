#Задача 7. Формат времени
seconds = int(input("Введите секунды: "))

minutes = seconds // 60
seconds = seconds % 60

print(f"{minutes} минута {seconds} секунд")