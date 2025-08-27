import math
from abc import ABC, abstractmethod


class Vector:
    __slots__ = ('x', 'y')

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> 'Vector':
        return Vector(self.x * other, self.y * other)

    def __truediv__(self, other: float) -> 'Vector':
        return Vector(self.x / other, self.y / other)

    def length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self) -> 'Vector':
        return self / self.length()


type Polar = tuple[float, float]


class Scene(ABC):
    def __init__(self, width: float, height: float):
        self.width: float = width
        self.height: float = height

    @abstractmethod
    def draw_arrow_vector(self, pivot: Vector, coords: Vector):
        ...
