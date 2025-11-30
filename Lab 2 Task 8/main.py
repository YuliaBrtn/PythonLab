#Дан список чисел. Удалите все элементы, которые делятся на 5 без остатка.
# numbers = [5, 12, 15, 20, 23, 25, 30, 33]
# result = []
# for num in numbers:
#     if num % 5 != 0:
#         result.append(num)
# print(f"Список после удаления кратных 5: {result}")
string1 = input("Введите строку с словами: ")

words = string1.split()

words_6 = []
for word in words:
    if len(word) == 6:
        words_6.append(word)

result_string = ' '.join(words_6)

print("\nИсходная строка:", string1)
print("Слова длиной 6 символов:", result_string)