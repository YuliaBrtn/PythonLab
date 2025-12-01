import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Создаем сетку данных
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Вычисляем функцию z = sin(sqrt(x^2 + y^2))
Z = np.sin(np.sqrt(X**2 + Y**2))

# Создаем 3D график
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

# Создаем поверхность
surface = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.9)

# Настройки графика
ax.set_title('3D график поверхности: z = sin(√(x² + y²))', fontsize=16, pad=20)
ax.set_xlabel('X', fontsize=12, labelpad=10)
ax.set_ylabel('Y', fontsize=12, labelpad=10)
ax.set_zlabel('Z', fontsize=12, labelpad=10)

# Добавляем цветовую шкалу
fig.colorbar(surface, ax=ax, shrink=0.6, aspect=20, label='Значения Z')

# Сохраняем в PNG и PDF
plt.savefig('3d_surface_plot.png', dpi=300, bbox_inches='tight')
plt.savefig('3d_surface_plot.pdf', bbox_inches='tight')

plt.show()