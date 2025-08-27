import drawsvg as dw

from visualization.draw.abstract import Scene, Vector


class SvgScene(Scene):
    def __init__(self, width: float, height: float):
        super().__init__(width, height)

        self.drawing = dw.Drawing(width, height, origin=(0, 0))

    def draw_arrow_vector(self, pivot: Vector, coords: Vector):
        start = pivot
        end = pivot + coords

        self.drawing.append(
            dw.Marker(
                ...
            )
        )

