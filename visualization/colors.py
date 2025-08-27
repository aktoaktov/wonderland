import matplotlib.colors as mcolors
import numpy as np

COLORS = {
    'red': '#e7000b',
    'orange': '#f54900',
    'yellow': '#f0b100',
    'green': '#5ea500',
    'emerald': '#009966',
    'teal': '#009689',
    'sky': '#0084d1',
    'blue': '#4f39f6',
    'purple': '#9810fa',
}


def gradient(color_start: str, color_end: str, n: int):
    color_start = COLORS.get(color_start, color_start)
    color_end = COLORS.get(color_end, color_end)

    start_rgb = np.array(mcolors.to_rgb(color_start))
    end_rgb = np.array(mcolors.to_rgb(color_end))

    return [start_rgb + (end_rgb - start_rgb) * i / (n - 1) for i in range(n)]
