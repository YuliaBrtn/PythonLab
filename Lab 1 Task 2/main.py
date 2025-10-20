#Задача 2. Удаление гласных
s = input()

for char in "aeiouAEIOU":
    s = s.replace(char, "")

print(s)