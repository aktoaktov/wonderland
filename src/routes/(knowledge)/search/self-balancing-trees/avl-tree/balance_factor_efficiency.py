import matplotlib.pyplot as plt
import numpy as np

from visualization import fig_ax
from visualization.colors import gradient

fig, ax = fig_ax()


def gen_time(b: int):
    phi = np.roots([1, -1] + [0] * (b - 3) + [-1])[0].real

    def time(n: int):
        return 1 / np.log(phi) * np.log(n) - 1 / np.log(phi) * phi ** 2 / (phi - 1) / (b * phi - b + phi) * 1 / np.log(
            phi) / n

    return time


bs = 20

colors = gradient('blue', 'red', bs)

x = np.linspace(1, 100_000, 1_000)

for b in range(1, bs + 1):
    y = np.vectorize(gen_time(b))(x)

    ax.plot(x, y, color=colors[b - 1])
    # ax.set_xscale('log')

    # if d in [2, 3, 4, 5, 10, 20]:
    #     plt.text(x[-1] + 10000, y[-1] - 0.2, f'{d}')

fig.show()
# fig.savefig('dary-heap-time.svg')
