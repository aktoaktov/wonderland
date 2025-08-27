import matplotlib.pyplot as plt
import numpy as np

from visualization import fig_ax
from visualization.colors import gradient

fig, ax = fig_ax()


def gen_insert_time(d: int):
    def insert_time(n: int):
        return np.log(n * (d - 1)) / np.log(d)

    return insert_time

ds = 20

colors = gradient('blue', 'red', ds-1)

x = np.linspace(1, 100_000, 1_000)

for d in range(2, ds+1):
    y = np.vectorize(gen_insert_time(d))(x)

    ax.plot(x, y, color=colors[d-2])
    ax.set_xscale('log')

    if d in [2, 3, 4, 5, 10, 20]:
        plt.text(x[-1] + 10000, y[-1] - 0.2, f'{d}')

fig.savefig('dary-heap-time.svg')
