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
            input.pop(index)  # important to use index and not value at index despite ()
        else:
            index += 1
    return max


# include if statement at the beginning to account for special case (empty list)
# max variable stores the highest value throughout the list
# only raise the index when pop is not happening because pop makes the list smaller
