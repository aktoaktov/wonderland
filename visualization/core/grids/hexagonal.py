import math
from typing import Iterator


def hex_grid(
        xrange: tuple[float, float],
        yrange: tuple[float, float],
        resolution: float
) -> Iterator[tuple[float, float]]:
    """
    Generates a hexagonal grid

    Parameters:
    xrange: (xmin: float, xmax: float) - bounding box of x-axis
    yrange: (ymin: float, ymax: float) - bounding box of y-axis
    resolution: resolution of hexagonal grid, points per unit length

    Yields:
    (x, y): (float, float) - coordinates of hexagonal grid
    """

    dx = 1.0 / resolution
    dy = math.sqrt(3) / 2 * dx

    nx = int((xrange[1] - xrange[0]) / dx) + 2
    ny = int((yrange[1] - yrange[0]) / dy) + 2

    for i in range(nx):
        for j in range(ny):
            x = xrange[0] + i * dx
            y = yrange[0] + j * dy

            if j % 2 == 1:
                x += dx / 2

            if xrange[0] <= x <= xrange[1] and yrange[0] <= y <= yrange[1]:
                yield x, y
