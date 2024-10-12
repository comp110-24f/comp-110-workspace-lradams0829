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


# since using while loop, variable called index is necessary
# include "or vals == []" so that while loop is entered if vals == []
# instead of recommendation in line 20, the if statement could be moved outside of loop


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


# since using while loop, variable called index is necessary
# max_val variable is helpful to keep track of the largest number
# else block not completely necessary, can move "index += 1" into if block


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """determine whether or not 2 lists are deep equals"""
    if len(list_1) != len(list_2):
        return False
    for index in range(0, len(list_1)):
        if list_1[index] != list_2[index]:
            return False
    return True


# use of for loop with range makes the code much shorter
# implement code that returns False right away if the lists aren't of equal length
# due to lines 36-37, range of only a single list is necessary


def extend(list_1: list[int], list_2: list[int]) -> None:
    """append the second list to the end of the first list"""
    for elem in list_2:
        list_1.append(elem)


# using for loop scans across every elem in list_2
# the loop finishes once the last elem of list_2 is added to list_1
