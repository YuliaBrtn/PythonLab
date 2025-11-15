#Создайте словарь, где ключами будут числа от 1 до N, а значениями — их количество делителей.
N = 10
divisors_dict = {}
for i in range(1, N + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    divisors_dict[i] = count
print(f"Словарь делителей для 1..{N}: {divisors_dict}")