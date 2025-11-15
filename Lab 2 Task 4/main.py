#Напишите программу, которая находит среднее арифметическое всех элементов списка.
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print(f"Среднее арифметическое: {average}")