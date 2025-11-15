#Дан кортеж строк. Найдите самую длинную строку в кортеже.
strings = ("apple", "banana", "cherry", "date", "elderberry")
longest = ""
for string in strings:
    if len(string) > len(longest):
        longest = string
print(f"Самая длинная строка: {longest}")