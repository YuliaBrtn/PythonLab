import matplotlib.pyplot as plt

# Данные о предпочтениях пользователей
categories = ['Социальные сети', 'Видео игры', 'Фильмы/Сериалы', 'Музыка', 'Книги']
preferences = [35, 25, 20, 15, 5]  # в процентах

# Цвета для каждой категории
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Создаем круговую диаграмму
plt.figure(figsize=(10, 8))
plt.pie(preferences, labels=categories, colors=colors, autopct='%1.1f%%', startangle=90)

# Добавляем заголовок
plt.title('Предпочтения пользователей по типам контента', fontsize=16, pad=20)

# Показываем график
plt.tight_layout()
plt.show()