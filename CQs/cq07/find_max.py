"""function find_and_remove_max defined"""

__author__ = "730750473"


def find_and_remove_max(input: list[int]) -> int:
    """return the largest number in the input and remove all instance of it"""
    if len(input) == 0:
        return -1
    max: int = 0
    index: int = 0
    while index < len(input):
        if input[index] >= max:
            max = input[index]
        index += 1
    index = 0
    while index < len(input):
        if input[index] == max:
            input.pop(index)
        else:
            index += 1
    return max
