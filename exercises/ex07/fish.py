"""File to define Fish class."""

__author__: str = "730750473"


class Fish:
    """Fish class with lone attribute age."""

    age: int

    def __init__(self):
        """Initializes Fish class."""
        self.age = 0

    def one_day(self) -> None:
        """Age gets 1 higher every day."""
        self.age += 1
