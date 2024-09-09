"""Practice with conditionals."""


def less_than_10(num: int) -> bool:
    """Tell me if num is < 10."""
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")


# less_than_10(num=8)


def should_i_eat(hungry: bool) -> None:
    """Tells me whether or not to eat based on hunger."""
    if hungry:
        print("EAT FOOD NOW")
    else:
        print("Take a nap!")


# should_i_eat(hungry=True)


def check_first_letter(word: str, letter: str) -> str:
    """The function checks if the first letter of a word matches the given letter."""
    if word[0] == letter:
        return "MATCH!"
    else:
        return "No match."


print(check_first_letter(word="happy", letter="h"))
print(check_first_letter(word="happy", letter="s"))
