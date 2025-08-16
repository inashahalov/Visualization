# Пример кода для matplotlib
import matplotlib.pyplot as plt

# Данные в MB
total = 16363492 / 1024  # ~15.98 GB
used = total - (6140540 / 1024)  # ~9.84 GB
available = 6140540 / 1024  # ~5.99 GB

labels = ['Использовано', 'Доступно']
sizes = [used, available]
colors = ['#ff9999', '#66b3ff']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Использование памяти')
plt.show()