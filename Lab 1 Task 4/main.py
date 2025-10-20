#Задача 4. Размен денег
summa = int(input("Введите сумму: "))

b100 = summa // 100
summa = summa % 100

b50 = summa // 50
summa = summa % 50

b10 = summa // 10
summa = summa % 10

b5 = summa // 5
summa = summa % 5

b2 = summa // 2
b1 = summa % 2

print(f"100: {b100}")
print(f"50: {b50}")
print(f"10: {b10}")
print(f"5: {b5}")
print(f"2: {b2}")
print(f"1: {b1}")