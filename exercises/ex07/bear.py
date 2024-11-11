"""File to define Bear class."""

__author__: str = "730750473"


class Bear:
    """Bear class with attributes age and hunger score"""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes Bear class."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        """Hunger gets 1 worse and age 1 higher every day."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Hunger score increases by number of fish eaten."""
        self.hunger_score += num_fish
