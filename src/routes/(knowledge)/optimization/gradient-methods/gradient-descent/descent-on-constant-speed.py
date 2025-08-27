import numpy as np
import matplotlib.pyplot as plt
\
from matplotlib.animation import FuncAnimation


def f(x, y):
    A = 0.5 * x ** 2 - 0.25 * y ** 2 + 3
    B = 2 * x + 1 - np.exp(y)
    return - np.sin(A) * np.cos(B)


def gradient(x, y):
    A = 0.5 * x ** 2 - 0.25 * y ** 2 + 3
    B = 2 * x + 1 - np.exp(y)

    dA_dx = x
    dA_dy = -0.5 * y
    dB_dx = 2
    dB_dy = -np.exp(y)

    df_dx = np.cos(A) * dA_dx * np.cos(B) + np.sin(A) * (-np.sin(B)) * dB_dx

    df_dy = np.cos(A) * dA_dy * np.cos(B) + np.sin(A) * (-np.sin(B)) * dB_dy

    return - np.array([df_dx, df_dy])


eta = np.linspace(0, 2, 100)
n_frames = len(eta)


def descent(leta):
    x = np.array([-0.25, 0.3])
    yield x
    for _ in range(30):
        x = x - leta * gradient(*x)
        yield x


x = np.linspace(-1.5, 2, 300)
y = np.linspace(-1.5, 2, 300)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig, ax = plt.subplots()
# ax.set_xlim(-1.5, 1.5)
# ax.set_ylim(-1.5, 1.5)

contour = ax.contour(X, Y, Z,
                     levels=80,
                     cmap='plasma',
                     linewidths=0.5,
                     antialiased=True)


line, = ax.plot([], [], 'b-', linewidth=2, markersize=8, label='Ломаная')
ax.legend()


def init():
    line.set_data([], [])
    return line,


def update(frame):
    current_points = np.array(list(descent(eta[frame])))
    x_data = current_points[:, 0]
    y_data = current_points[:, 1]

    line.set_data(x_data, y_data)

    plt.title(eta[frame])
    return line,


ani = FuncAnimation(
    fig,
    update,
    frames=n_frames,
    init_func=init,
    blit=True,
    interval=200,
    # repeat=False
)

plt.tight_layout()
plt.show()
