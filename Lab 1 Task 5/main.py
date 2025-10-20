#Задача 5. Магическое число
n = int(input("Введите число: "))

if n % 7 == 0:
    print("Магическое число!")
else:
    # Считаем сумму цифр
    s = 0
    for digit in str(n):
        s += int(digit)
    print(s)