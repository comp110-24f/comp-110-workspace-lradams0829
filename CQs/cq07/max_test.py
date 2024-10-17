"""function find_and_remove_max tested"""

__author__ = "730750473"


from CQs.cq07.find_max import find_and_remove_max

# import function before testing


# desired return value
def test_function_return_value() -> None:
    """find_and_remove_max should return max"""
    special_input: list[int] = [2, 4, 6, 4, 6, 5, 1]
    assert find_and_remove_max(special_input) == 6


# desired list alteration
def test_function_mutate() -> None:
    """find_and_remove_max should remove all instances of max from list"""
    special_input: list[int] = [2, 4, 6, 4, 6, 5, 1]
    find_and_remove_max(special_input)
    # call the function first so the assert statement provides the updated list
    assert special_input == [2, 4, 4, 5, 1]


# edge case, empty list
def test_edge_case() -> None:
    """find_and_remove_max should return -1 when given an empty list"""
    assert find_and_remove_max([]) == -1
