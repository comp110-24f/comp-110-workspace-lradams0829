"""ex02 - Chardle - a little step toward Wordle!"""

__author__: str = "730750473"


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    if 5 != len(word):
        print("Error: Word must contain 5 characters.")
    return word


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if not 1 == len(letter):
        print("Error: Character must be a single character.")
    return letter


def contains_char(word: str, letter: str) -> None:
    if word == input_word and letter == input_letter:
        
    print("Searching for " + letter + " in " + word)


# how to import code for use in the REPL:
# from exercises.ex02_chardle import input_function
