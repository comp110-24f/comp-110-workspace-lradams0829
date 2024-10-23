"""This is my code for the ex05 functions!"""

__author__: str = "730750473"


def only_evens(input: list[int]) -> list[int]:
    """given a list, return only the even values in a new list"""
    empty_list = []  # add even values to empty list so that input isn't mutated
    index: int = 0
    while index < len(input):
        if input[index] % 2 == 0:  # even numbers divided by 2 have a remainder of 0
            empty_list.append(input[index])  # append wants the value and not the index
        index += 1  # index increases regardless because using append
    return empty_list


# when using pop, index does not increase in the if block because the list loses length


def sub(input: list[int], start: int, end: int) -> list[int]:
    """return list of values between the indexes 'start' and 'end' - 1 of input list"""
    # 'end' - 1 because end index is NOT inclusive
    if len(input) == 0 or start >= len(input) or end <= 0:
        return []
    # cannot start at index past input length, negative index doesn't work
    if start < 0:
        start = 0
    # start index can be 0 at the lowest
    if end > len(input):
        end = len(input)
    # end index can be the input length at the longest
    return input[start:end]
    # end index is NOT inclusive, [1:5] covers indexes 1, 2, 3, 4


# nothing is looped over in this case, if statements simply account for edge cases
# input list isn't mutated because the list is only referenced in the return statement


def add_at_index(input: list[int], element: int, index: int) -> None:
    """given a list, add element at a particular index of the list"""
    if index > len(input) or index < 0:
        raise IndexError("Index is out of bounds for the input list")
    elif index == len(input):
        # [len(input) - 1] is the last index, so just add on to end
        input.append(element)
        # append adds element to end of input 'input.append(element)'
        # pop removes element at end of input 'input.pop()'
        # pop can also remove the element at inserted index 'input.pop(index)'
    else:
        input.append(999)
        # obscure 999 serves as a placeholder at end of list
        for idx in range(len(input) - 1, index, -1):  # range(start, stop, step)
            # 'len(input) - 1' is the index of the last element (placeholder)
            # -1 step means range of indexes starts at placeholder and ends before index
            input[idx] = input[idx - 1]
            # changes the placeholder element to the value of the element to its left
            # loops until index is reached
        input[index] = element  # now can simply change the element at desired index


# example of process:
# add_at_index([6, 6, 9, 2], 5, 1) should result in [6, 5, 6, 9, 2]
# input.append(999), input = [6, 6, 9, 2, 999]
# len(input) - 1 = 4 (999 in the list), index = 1
# compute input[idx] = input[idx - 1] for idx = 4, 3, 2
# input[4] = input[3], input = [6, 6, 9, 2, 2]
# input[3] = input[2], input = [6, 6, 9, 9, 2]
# input[2] = input[1], input = [6, 6, 6, 2, 2]
# change index 1 from element value 6 to 5, input = [6, 5, 6, 9, 2]
