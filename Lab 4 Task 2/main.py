import numpy as np
import matplotlib.pyplot as plt

# Генерируем данные для трех кластеров
np.random.seed(42)  # Для воспроизводимости результатов

# Первый кластер
x1 = np.random.normal(2, 0.5, 50)
y1 = np.random.normal(2, 0.5, 50)

# Второй кластер
x2 = np.random.normal(4, 0.3, 50)
y2 = np.random.normal(1, 0.4, 50)

# Третий кластер
x3 = np.random.normal(1, 0.6, 50)
y3 = np.random.normal(4, 0.5, 50)

# Создаем график
plt.figure(figsize=(10, 8))

# Создаем точечную диаграмму с разными цветами для каждого кластера
plt.scatter(x1, y1, color='red', alpha=0.7, label='Кластер 1', s=50)
plt.scatter(x2, y2, color='blue', alpha=0.7, label='Кластер 2', s=50)
plt.scatter(x3, y3, color='green', alpha=0.7, label='Кластер 3', s=50)

# Настраиваем график
plt.title('Точечная диаграмма с тремя кластерами данных', fontsize=14, pad=20)
plt.xlabel('X значения', fontsize=12)
plt.ylabel('Y значения', fontsize=12)
plt.legend(fontsize=10, loc='upper right')
plt.grid(True, alpha=0.3)

# Устанавливаем равные масштабы по осям для корректного отображения
plt.axis('equal')

# Показываем график
plt.tight_layout()
plt.show()