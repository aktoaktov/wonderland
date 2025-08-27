from typing import Callable, Tuple

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler

mpl.rcParams['axes.prop_cycle'] = cycler(
    color=['#2b7fff', '#fb2c36', '#f0b100', '#00c950', '#00bba7', '#ad46ff', '#f6339a'])


VECTOR_ARROW_WIDTH = 0.002





def simple_function(func: Callable[[float, ], float],
                    xrange: tuple[float, float],
                    precision: int = 500,
                    title: str | None = None) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(10, 6))

    x = np.linspace(xrange[0], xrange[1], precision)
    y = np.vectorize(func)(x)

    ax.plot(x, y)

    ax.grid(which='major', linestyle='-', linewidth=0.8, alpha=0.9)
    ax.set_xticks(np.arange(np.floor(xrange[0]), np.ceil(xrange[1]) + 1, 1))
    ax.set_yticks(np.arange(np.floor(y.min()), np.ceil(y.max()) + 1, 1))

    ax.grid(which='minor', linestyle=':', linewidth=0.5, alpha=0.9)
    ax.set_xticks(np.arange(xrange[0], xrange[1] + 0.1, 0.25), minor=True)
    ax.set_yticks(np.arange(np.floor(y.min()), np.ceil(y.max()) + 0.1, 0.25), minor=True)

    ax.set_title(title)

    plt.tight_layout()
    return fig


def vector_field_2d(
        field: Callable[[float, float], tuple[float, float]],
        x_range: tuple[float, float],
        y_range: tuple[float, float],

        resolution: int = 30,
        title: str | None = None
) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(10, 6))

    x = np.linspace(x_range[0], x_range[1], resolution)
    y = np.linspace(y_range[0], y_range[1], resolution)
    xx, yy = np.meshgrid(x, y)

    field_x, field_y = np.vectorize(field)(xx, yy)

    magnitudes = np.sqrt(field_x ** 2 + field_y ** 2)

    with np.errstate(divide='ignore', invalid='ignore'):
        field_x_norm = np.where(magnitudes != 0, field_x / magnitudes * (np.exp(- (magnitudes - 3) ** 2) + 1), 0)
        field_y_norm = np.where(magnitudes != 0, field_y / magnitudes * (np.exp(- (magnitudes - 3) ** 2) + 1), 0)
    field_x, field_y = field_x_norm, field_y_norm

    magnitudes = (magnitudes - magnitudes.min()) / (magnitudes.max() - magnitudes.min() + 1e-10)

    ax.quiver(xx, yy, field_x, field_y, magnitudes,
              width=VECTOR_ARROW_WIDTH,
              headwidth=3,
              headlength=2.5,
              headaxislength=2
              )

    plt.tight_layout()
    return fig
