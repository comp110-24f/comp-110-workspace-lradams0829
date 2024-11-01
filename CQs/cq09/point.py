# the following line must be at the top
from __future__ import annotations

"""challenge question for introduction to object-oriented programming"""

__author__: str = "730750473"


class Point:
    x: float
    y: float
    # x and y are attributed

    # setting up constructor
    def __init__(self, x_init: float, y_init: float):
        # return is intuitive, no need for type
        self.x = x_init
        self.y = y_init
        # initialization format: self.attribute = value

    # method definition (mutate)
    def scale_by(self, factor: int) -> None:
        self.x *= factor
        self.y *= factor
        # self.x and self.y are accessed directly and mutated

    # method definition (don't mutate)
    def scale(self, factor: int) -> Point:
        return Point(self.x * factor, self.y * factor)
        # self.x and self.y are only referenced in the new Point
