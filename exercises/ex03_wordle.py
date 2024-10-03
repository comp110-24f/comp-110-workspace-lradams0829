"""The dreaded beast of an exercise awaits you!"""

__author__ = "730750473"


def input_guess(secret_word_len: int) -> str:
    """function to check that user inputs the correct number of letters in guess"""
    word_guess: str = input(f"Enter a {secret_word_len} character word: ")
    while len(word_guess) != secret_word_len:
        word_guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
        if len(word_guess) == secret_word_len:
            return word_guess
    return word_guess


# f-strings used for ease
# initial while loop evaluates to False, it exits to return word_guess
# initial while loop evaluates to True, it enters the loop and prompts for user to input
# if statement evaluates to False, it exits back to prompting user to input
# if statement evaluates to True, it enters to return word_guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """function to check whether or not a word contains a specific character"""
    assert len(char_guess) == 1
    index: int = 0
    while index < len(secret_word):
        if char_guess != secret_word[index]:
            index += 1
        else:
            return True
    return False


# indexing using a relational expression allows the loop to end
# if index becomes greater than the word length, the function returns False
# if the character is found before the index gets too high, the function returns True


def emojified(guess: str, secret: str) -> str:
    """function to provide user with insight regarding the guess word's accuracy"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    tally: str = ""
    emoji_index: int = 0
    while emoji_index < len(guess):
        if guess[emoji_index] == secret[emoji_index]:
            tally += GREEN_BOX
        elif contains_char(secret, guess[emoji_index]):
            tally += YELLOW_BOX
        else:
            tally += WHITE_BOX
        emoji_index += 1
    return tally


#
