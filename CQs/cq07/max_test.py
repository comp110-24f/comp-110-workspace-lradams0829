"""function find_and_remove_max tested"""

__author__ = "730750473"


from CQs.cq07.find_max import find_and_remove_max


def test_function_return_value() -> None:
    """find_and_remove_max should return max"""
    special_input: list[int] = [2, 4, 6, 4, 6, 5, 1]
    assert find_and_remove_max(special_input) == 6
