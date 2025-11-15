#Напишите программу, которая подсчитывает количество согласных букв в строке.
text = "Hello World!"
consonants = "bcdfghjklmnpqrstvwxyz"
count = 0
for char in text.lower():
    if char in consonants:
        count += 1
print(f"Количество согласных в '{text}': {count}")