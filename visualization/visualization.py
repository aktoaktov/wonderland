import numpy as np
from matplotlib import pyplot as plt


def fig_ax(
        title: str = None,
):
    fig, ax = plt.subplots(figsize=(6, 4))

    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = 'Computer Modern Roman'
    plt.rcParams['font.sans-serif'] = 'Computer Modern Roman'
    plt.rcParams['font.size'] = 14

    ax.tick_params(axis='both', which='major', labelsize=14)
    ax.tick_params(axis='both', which='minor', labelsize=12)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)

    if title is not None:
        ax.set_title(title)

    plt.tight_layout()
    return fig, ax
