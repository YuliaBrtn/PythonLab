#Задача 13. Угадай число
import random

number = random.randint(1, 100)

while True:
    guess = int(input("Ваша догадка: "))

    if guess < number:
        print("Больше")
    elif guess > number:
        print("Меньше")
    else:
        print("Угадал!")
        break