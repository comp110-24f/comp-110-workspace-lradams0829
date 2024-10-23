"""These are my unit test functions for ex05!"""

__author__: str = "730750473"


from exercises.ex05.utils import only_evens, sum, add_at_index
import pytest


# desired list alteration
def test_add_at_index_mutate() -> None:
    """tests whether add_at_index will alter the list correctly"""
    awesome_list: list[int] = [6, 6, 9, 2]
    add_at_index(awesome_list, 5, 1)
    # call function before assert line so that mutation is made
    assert awesome_list == [6, 5, 6, 9, 2]
