def get_first(input: list[str]) -> str:
    """function that returns first element in a list of strings"""
    if len(input) == 0:
        return ""
    return input[0]


def remove_first(input: list[str]) -> None:
    """function that removes first element in a list"""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """function that returns first element and removes it from a list of strings"""
    return input.pop(0)
