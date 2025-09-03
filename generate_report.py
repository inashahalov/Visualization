# generate_report.py
# Сбор системной информации и экспорт в HTML + PDF
# Автор: inashakhalov | 2025-04-05

import os
import matplotlib.pyplot as plt
from datetime import datetime

# Создаём папку для графиков
os.makedirs("graphs", exist_ok=True)

# ========================================
# 1. Данные (имитация /proc/meminfo и /proc/cpuinfo)
# ========================================

# Память в KB
mem_total_kb = 16363492
mem_free_kb = 1650540
mem_available_kb = 6140540
buffers_kb = 191508
cached_kb = 9184540
active_kb = 11482708
inactive_kb = 2207648

# В MB
total_mb = mem_total_kb / 1024
used_mb = total_mb - (mem_available_kb / 1024)
available_mb = mem_available_kb / 1024
buffers_mb = buffers_kb / 1024
cached_mb = cached_kb / 1024
active_mb = active_kb / 1024
inactive_mb = inactive_kb / 1024

# Swap
swap_total_mb = 4096
swap_used_mb = 0
swap_free_mb = swap_total_mb

# CPU
cpu_info = {
    "bogomips": "6215.96",
    "clflush_size": "64 bytes",
    "cache_alignment": "64 bytes",
    "address_sizes": "36/48 bits"
}

# ========================================
# 2. Графики
# ========================================

# Круговая диаграмма: Использование RAM
plt.figure(figsize=(6, 4))
labels = ['Использовано', 'Доступно']
sizes = [used_mb, available_mb]
colors = ['#ff6666', '#66b3ff']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title("Использование оперативной памяти")
plt.tight_layout()
plt.savefig("graphs/pie_memory.png")
plt.close()

# Столбчатая диаграмма: Детали памяти
plt.figure(figsize=(10, 5))
components = ['Total', 'Used', 'Available', 'Cached', 'Buffers', 'Active', 'Inactive']
values = [total_mb, used_mb, available_mb, cached_mb, buffers_mb, active_mb, inactive_mb]
colors = ['#444444', '#e74c3c', '#2ecc71', '#3498db', '#f39c12', '#8e44ad', '#34495e']

bars = plt.bar(components, values, color=colors)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 50,
             f'{int(height)}', ha='center', va='bottom', fontsize=9)

plt.title("Распределение памяти (MB)")
plt.ylabel("Объём (MB)")
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig("graphs/bar_memory.png")
plt.close()

# ========================================
# 3. HTML-отчёт
# ========================================

html_content = f"""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Системный отчёт — {datetime.now().strftime('%d.%m.%Y')}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            background: #f4f6f9;
            color: #333;
            margin: 40px;
            line-height: 1.6;
        }}
        h1, h2, h3 {{
            color: #003366;
        }}
        .header {{
            background: #003366;
            color: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ccc;
            padding: 10px;
            text-align: left;
        }}
        th {{
            background-color: #0055cc;
            color: white;
        }}
        img {{
            max-width: 100%;
            height: auto;
            border-radius: 6px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        .section {{
            background: white;
            padding: 20px;
            margin: 20px 0;
            border-radius: 6px;
            box-shadow: 0 1px 5px rgba(0,0,0,0.1);
        }}
        footer {{
            text-align: right;
            font-size: 0.9em;
            color: #666;
            margin-top: 40px;
        }}
    </style>
</head>
<body>

    <div class="header">
        <h1>🖥️ Системный отчёт</h1>
        <p><strong>Дата:</strong> {datetime.now().strftime('%d.%m.%Y %H:%M')} | <strong>Генератор:</strong> inashakhalov</p>
    </div>

    <div class="section">
        <h2>1. Информация о процессоре</h2>
        <table>
            <tr><th>Параметр</th><th>Значение</th></tr>
            <tr><td>bogomips</td><td>{cpu_info['bogomips']}</td></tr>
            <tr><td>clflush size</td><td>{cpu_info['clflush_size']}</td></tr>
            <tr><td>cache_alignment</td><td>{cpu_info['cache_alignment']}</td></tr>
            <tr><td>address sizes</td><td>{cpu_info['address_sizes']}</td></tr>
        </table>
    </div>

    <div class="section">
        <h2>2. Использование памяти</h2>
        <p><strong>Всего:</strong> {total_mb:.0f} MB | <strong>Использовано:</strong> {used_mb:.0f} MB | <strong>Доступно:</strong> {available_mb:.0f} MB</p>
        <img src="graphs/pie_memory.png" alt="Круговая диаграмма использования памяти">
    </div>

    <div class="section">
        <h2>3. Детализация памяти (MB)</h2>
        <table>
            <tr><th>Компонент</th><th>Значение (MB)</th><th>% от общего</th></tr>
            <tr><td>MemTotal</td><td>{total_mb:.0f}</td><td>100%</td></tr>
            <tr><td>MemFree</td><td>{mem_free_kb/1024:.0f}</td><td>{(mem_free_kb/mem_total_kb)*100:.1f}%</td></tr>
            <tr><td>MemAvailable</td><td>{available_mb:.0f}</td><td>{(mem_available_kb/mem_total_kb)*100:.1f}%</td></tr>
            <tr><td>Buffers</td><td>{buffers_mb:.0f}</td><td>{(buffers_kb/mem_total_kb)*100:.1f}%</td></tr>
            <tr><td>Cached</td><td>{cached_mb:.0f}</td><td>{(cached_kb/mem_total_kb)*100:.1f}%</td></tr>
            <tr><td>Active</td><td>{active_mb:.0f}</td><td>{(active_kb/mem_total_kb)*100:.1f}%</td></tr>
            <tr><td>Inactive</td><td>{inactive_mb:.0f}</td><td>{(inactive_kb/mem_total_kb)*100:.1f}%</td></tr>
        </table>
        <img src="graphs/bar_memory.png" alt="Столбчатая диаграмма памяти">
    </div>

    <div class="section">
        <h2>4. Swap-пространство</h2>
        <table>
            <tr><th>Компонент</th><th>Значение</th><th>%</th></tr>
            <tr><td>Total</td><td>{swap_total_mb} MB</td><td>100%</td></tr>
            <tr><td>Used</td><td>{swap_used_mb} MB</td><td>0%</td></tr>
            <tr><td>Free</td><td>{swap_free_mb} MB</td><td>100%</td></tr>
        </table>
        <p>✅ <strong>Swap не используется</strong> — система стабильна.</p>
    </div>

    <footer>
        Отчёт сгенерирован автоматически | inashakhalov@vtb.ru
    </footer>

</body>
</html>
"""

# Сохраняем HTML
with open("report.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ HTML-отчёт сохранён: report.html")

# ========================================
# 4. Конвертация HTML → PDF
# ========================================

try:
    from weasyprint import HTML
    HTML("report.html").write_pdf("report.pdf")
    print("✅ PDF-отчёт сохранён: report.pdf")
except Exception as e:
    print(f"❌ Ошибка при генерации PDF: {e}")
    print("Установите WeasyPrint: pip install weasyprint")
    print("Или установите: sudo apt install libpango-1.0-0 libharfbuzz0b libcairo2")