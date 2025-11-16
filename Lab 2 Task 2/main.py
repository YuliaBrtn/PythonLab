#Дан список чисел. Удалите из него все чётные числа.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = []
for num in numbers:
    if num % 2 != 0:
        result.append(num)
print(f"Список без чётных чисел: {result}")