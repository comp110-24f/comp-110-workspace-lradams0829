"""Chardle - a step toward Wordle!"""

__author__: str = "730750473"


def input_word() -> str:
    char_length: int = 5
    word: str = str(input("Enter a 5-character word: "))
    if char_length != len(word):
        print("Error: Word must contain 5 characters.")
    else:
        print(None)
    return word
