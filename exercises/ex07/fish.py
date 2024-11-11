"""File to define Fish class."""


class Fish:
    age: int

    def __init__(self):
        self.age = 0

    def one_day(self) -> None:
        """age gets 1 higher every day"""
        self.age += 1
