import matplotlib.pyplot as plt
import numpy as np

# Данные для диаграммы
categories = ['Продукт A', 'Продукт B', 'Продукт C', 'Продукт D', 'Продукт E']
values = [23, 45, 56, 78, 32]

# Создаем горизонтальную столбчатую диаграмму
plt.figure(figsize=(10, 6))
bars = plt.barh(categories, values, color='skyblue', alpha=0.7)

# Добавляем значения на столбцы
for bar, value in zip(bars, values):
    width = bar.get_width()
    plt.text(width + 1, bar.get_y() + bar.get_height()/2,
             f'{value}', ha='left', va='center', fontweight='bold')

# Настройки графика
plt.title('Горизонтальная столбчатая диаграмма\nПродажи по продуктам', fontsize=14, pad=20)
plt.xlabel('Количество продаж', fontsize=12)
plt.ylabel('Продукты', fontsize=12)
plt.grid(True, axis='x', alpha=0.3)
plt.tight_layout()
plt.show()

# Сохраняем в PNG и PDF
plt.savefig('scatter_plot.png', dpi=300, bbox_inches='tight')
plt.savefig('scatter_plot.pdf', bbox_inches='tight')
plt.close()  # Закрываем фигуру