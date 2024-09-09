"""This exercise is to plan a tea party, which will help me understand functions."""

__author__: str = "730750473"


def tea_bags(people: int) -> int:
    """This function declares the number of people at the tea party."""
    return people * 2  # Two tea bags per guest, so multiply people by two.


def treats(people: int) -> int:
    """This function helps find the number of treats based on teas expected."""
