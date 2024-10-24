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


# alter empty list
def test_add_at_index_empty_list() -> None:
    """tests whether add_at_index will alter the empty list correctly"""
    empty_list: list[int] = []
    add_at_index(empty_list, 5, 0)
    # empty_list should no longer be empty
    assert empty_list == [5]


# edge case, IndexError
def test_add_at_index_edge_case() -> None:
    """tests whether an IndexError is raised"""
    awesome_list: list[int] = [6, 6, 9, 2]
    with pytest.raises(IndexError):
        add_at_index(awesome_list, 5, 999)
    # pytest checks whether correct exception (IndexError) is triggered


# start < 0
def test_sum_low_start() -> None:
    """tests whether start < 0 changes start to 0"""
    cool_list: list[int] = [1, 2, 3, 4, 9, 8, 7]
    assert sum(cool_list, -3, 4) == [1, 2, 3, 4]


# end > len(input)
def test_sum_high_end() -> None:
    """tests whether end > len(input) changes end to len(input)"""
    cool_list: list[int] = [1, 2, 3, 4, 9, 8, 7]
    assert sum(cool_list, 4, 8) == [9, 8, 7]


# edge case, len(input) == 0
def test_sum_edge_case() -> None:
    """tests whether input empty list returns an empty list"""
    not_so_cool_list: list[int] = []
    assert sum(not_so_cool_list, 0, 2) == []


# list of only odds
def test_only_evens_odd_list() -> None:
    """tests whether a list of only odds returns an empty list"""
    list_of_odds: list[int] = [1, 7, 7, 9, 5, 3]
    assert only_evens(list_of_odds) == []


# no list alteration
def test_only_evens_no_mutate() -> None:
    """tests whether input list isn't mutated"""
    rad_list: list[int] = [4, 5, 6, 2, 0, 1]
    only_evens(rad_list)  # call function before assert line to see if mutation is made
    assert rad_list == [4, 5, 6, 2, 0, 1]


# edge case, empty list
def test_only_evens_empty_list() -> None:
    """tests whether input empty list returns an empty list"""
    lame_list: list[int] = []
    assert only_evens(lame_list) == []
