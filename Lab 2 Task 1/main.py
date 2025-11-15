def multiply_digits(n):
    product = 1
    for digit in str(n):
        if digit.isdigit():
            product *= int(digit)
    return product

N = 5981
print(f"Произведение цифр {N}: {multiply_digits(N)}")
