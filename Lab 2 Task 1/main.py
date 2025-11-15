def multiply_digits(n):
    product = 1
    # Используем цикл for для итерации по строке
    for digit in str(n):
        if digit.isdigit():
            product *= int(digit)
    return product

N = 1234
print(f"Произведение цифр {N}: {multiply_digits(N)}")
