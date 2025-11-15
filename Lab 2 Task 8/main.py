#Дан список чисел. Удалите все элементы, которые делятся на 5 без остатка.
numbers = [5, 12, 15, 20, 23, 25, 30, 33]
result = []
for num in numbers:
    if num % 5 != 0:
        result.append(num)
print(f"Список после удаления кратных 5: {result}")
