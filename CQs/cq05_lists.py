"""Mutating functions."""

__author__ = "730750473"


def manual_append(original_list: list[int], new_item: int) -> None:
    """function adds new_item to the end of original_list"""
    original_list.append(new_item)
    return None


def double(original_list: list[int]) -> None:
    """function multiplies each list item by 2"""
    index: int = 0
    while index < len(original_list):
        original_list[index] *= 2
        index += 1
    return None


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
