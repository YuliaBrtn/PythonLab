#Создайте программу, которая удаляет из словаря все ключи, значения которых меньше 10.
my_dict = {"a": 5, "b": 15, "c": 8, "d": 20, "e": 3}
keys_to_remove = []
for key, value in my_dict.items():
    if value < 10:
        keys_to_remove.append(key)
for key in keys_to_remove:
    my_dict.pop(key)
print(f"Словарь после удаления: {my_dict}")