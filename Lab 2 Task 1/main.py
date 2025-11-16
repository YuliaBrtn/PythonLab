#Напишите программу, которая вычисляет произведение всех цифр числа N.
N = 5981
number_str = str(N)
product = 1

for digit in number_str:
    if digit.isdigit():
        product *= int(digit)

print(f"Произведение цифр {N}: {product}")
