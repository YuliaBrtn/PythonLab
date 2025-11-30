import numpy as np
import matplotlib.pyplot as plt

# Создаем матрицу 10x10 случайных чисел
data = np.random.rand(10, 10)

# Создаем тепловую карту
plt.figure(figsize=(10, 8))
heatmap = plt.imshow(data, cmap='viridis')

# Добавляем цветовую шкалу
plt.colorbar(heatmap, label='Значения')

# Настройки графика
plt.title('Тепловая карта 10x10 случайных чисел', fontsize=14, pad=20)
plt.xlabel('Столбцы', fontsize=12)
plt.ylabel('Строки', fontsize=12)

# Добавляем подписи значений на клетках
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        plt.text(j, i, f'{data[i, j]:.2f}',
                ha='center', va='center',
                color='white' if data[i, j] > 0.5 else 'black',
                fontsize=8)

plt.tight_layout()
plt.show()
