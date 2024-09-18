"""Practicing with while loops!"""

__author__ = "730750473"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0
    while index < len(phrase):  # str of len=3 only evaluates up until index=2
        if search_char == phrase[index]:
            count += 1  # count only increases when character matches
        index += 1  # occurs every time until end of phrase
    return count  # this is the number of instances that a character occurs
