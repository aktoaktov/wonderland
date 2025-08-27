import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection


def hex_grid(radius, size):
    """Генерирует центры шестиугольников"""
    q = np.arange(-size, size + 1)
    r = np.arange(-size, size + 1)
    Q, R = np.meshgrid(q, r)

    # Преобразование шестиугольных координат в декартовы
    x = radius * (np.sqrt(3) * Q + np.sqrt(3) / 2 * R)
    y = radius * (3 / 2 * R)

    # Фильтрация выходящих за пределы круга
    mask = (np.abs(Q + R) <= size) & (np.abs(Q) <= size) & (np.abs(R) <= size)
    return x[mask], y[mask]


def plot_hex_vector_field(F, radius=0.5, size=10):
    fig, ax = plt.subplots(figsize=(10, 10))

    # Генерация сетки
    x, y = hex_grid(radius, size)

    # Вычисление векторного поля
    Fx, Fy = np.vectorize(F)(x, y)

    # Нормализация длин
    lengths = np.sqrt(Fx ** 2 + Fy ** 2)
    Fx_norm = Fx / (lengths + 1e-10) * radius * 0.8
    Fy_norm = Fy / (lengths + 1e-10) * radius * 0.8

    # Цветовая карта
    colors = plt.cm.viridis(lengths / lengths.max())

    # Рисование стрелок
    for xi, yi, fxi, fyi, color in zip(x, y, Fx_norm, Fy_norm, colors):
        ax.arrow(xi, yi, fxi, fyi,
                 head_width=radius * 0.3,
                 head_length=radius * 0.4,
                 fc=color,
                 ec='none',
                 alpha=0.8)

    # Отрисовка шестиугольников (опционально)
    hex_lines = []
    for xi, yi in zip(x, y):
        hex_verts = []
        for angle in np.linspace(0, 2 * np.pi, 7):
            hex_verts.append([xi + radius * np.cos(angle),
                              yi + radius * np.sin(angle)])
        hex_lines.append(hex_verts[:-1])

    lc = LineCollection(hex_lines, colors='lightgray', linewidths=0.5, alpha=0.3)
    ax.add_collection(lc)

    ax.set_aspect('equal')
    plt.colorbar(plt.cm.ScalarMappable(cmap='viridis'), ax=ax, label='Magnitude')
    plt.show()


# Пример векторного поля
def vortex_field(x, y):
    return -y / (x ** 2 + y ** 2 + 0.1), x / (x ** 2 + y ** 2 + 0.1)


plot_hex_vector_field(vortex_field, radius=0.5, size=15)
plot_hex_vector_field(vortex_field, radius=1, size=15)
plot_hex_vector_field(vortex_field, radius=4, size=15)
plot_hex_vector_field(vortex_field, radius=8, size=15)

