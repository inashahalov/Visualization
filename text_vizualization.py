#!/usr/bin/env python3

# Простая текстовая визуализация без внешних библиотек
def print_memory_info():
    # Имитация данных из /proc/meminfo (в kB)
    mem_total = 16363492
    1649704
    mem_available = 6140540
    cached = 9184412
    buffers = 191852

    # Конвертация в MB
    total_mb = mem_total / 1024
    available_mb = mem_available / 1024
    cached_mb = cached / 1024
    buffers_mb = buffers / 1024
    used_mb = total_mb - available_mb

    print("=" * 50)
    print("           СИСТЕМА ПАМЯТИ")
    print("=" * 50)
    print(f"Общий объем памяти:     {total_mb:>8.1f} MB")
    print(f"Использовано:          {used_mb:>8.1f} MB ({(used_mb / total_mb) * 100:>5.1f}%)")
    print(f"Доступно:              {available_mb:>8.1f} MB ({(available_mb / total_mb) * 100:>5.1f}%)")
    print(f"Кэшировано:            {cached_mb:>8.1f} MB ({(cached_mb / total_mb) * 100:>5.1f}%)")
    print(f"Буферы:                {buffers_mb:>8.1f} MB ({(buffers_mb / total_mb) * 100:>5.1f}%)")
    print("=" * 50)

    # Текстовый график
    print("\nВизуализация использования памяти:")
    print("Использовано [", end="")
    used_bars = int((used_mb / total_mb) * 30)
    print("█" * used_bars + " " * (30 - used_bars) + f"] {used_mb / total_mb * 100:.1f}%")

    print("Доступно     [", end="")
    avail_bars = int((available_mb / total_mb) * 30)
    print("░" * avail_bars + " " * (30 - avail_bars) + f"] {available_mb / total_mb * 100:.1f}%")


if __name__ == "__main__":
    print_memory_info()