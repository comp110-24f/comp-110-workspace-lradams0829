"""summing the elements of a list using different loops"""

__author__ = "730750473"


def w_sum(vals: list[float]) -> float:
    """sums the elements of vals using while loop"""
    total: float = 0.0
    index: int = 0
    while index < len(vals):
        total += vals[index]
        index += 1
    return total


# local variable total is important to hold a tally
# index is necessary in while loop
# if len(vals) == 0, it is an empty list and avoids the while loop to return 0.0


def f_sum(vals: list[float]) -> float:
    """sums the elements of vals using for loop"""
    total: float = 0.0
    for elem in vals:
        total += elem
    return total


# local variable total is still necessary to hold a tally for return statement
# index no longer needed because elem goes straight to the source
# total += elem reassigns new value to total before re-entering for loop


def f_range_sum(vals: list[float]) -> float:
    """sums the elements of vals using for loop w/ range"""
    total: float = 0.0
    for index in range(0, len(vals)):
        total += vals[index]
    return total


# local variable total is still necessary to hold a tally for return statement
# index used but linked with the range of vals, no need to define as a local variable
# uses index like in the while loop, but saves some lines of code
