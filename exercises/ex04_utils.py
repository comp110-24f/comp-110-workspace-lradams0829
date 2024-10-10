"""list-oriented utility functions"""

__author__ = "730750473"


def all(vals: list[int], val: int) -> bool:
    """check to see if all the elements of a list are the given int"""
    index: int = 0
    while index < len(vals) or vals == []:
        if vals == []:
            return False
        elif val == vals[index]:
            index += 1
        else:
            return False
    return True


def max(vals: list[int]) -> int:
    """find and return the largest int in the list"""
    if len(vals) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 0
    max_val: int = vals[0]
    while index < len(vals):
        if vals[index] >= max_val:
            max_val = vals[index]
        else:
            max_val = max_val
        index += 1
    return max_val


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """determine whether or not 2 lists are deep equals"""
