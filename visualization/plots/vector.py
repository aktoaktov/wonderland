from typing import Callable

from visualization.core.constants import DEFAULT_VECTOR_FIELD_RESOLUTION


def vector_field_plot(
        field: Callable[[float, float], tuple[float, float]],
        xrange: tuple[float, float],
        yrange: tuple[float, float],
        resolution: int = DEFAULT_VECTOR_FIELD_RESOLUTION,
) -> Scene:


