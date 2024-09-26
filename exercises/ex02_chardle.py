"""ex02 - Chardle - a little step toward Wordle!"""

__author__: str = "730750473"


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    if 5 != len(word):
        print("Error: Word must contain 5 characters.")
        exit()  # exit() cuts the function off here
    # else:
    #  print(word)
    return word


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if not 1 == len(letter):
        print("Error: Character must be a single character.")
        exit()  # exit() cuts the function off here
    # else:
    # print("Enter a single character " + letter)  #
    return letter


def contains_char(word: str, letter: str) -> None:
    count: int = 0  # the word starts with 0 characters known
    print("Searching for " + letter + " in " + word)
    if letter == word[0]:
        print(letter + " found at index 0")
        count += 1
    if letter == word[1]:
        print(letter + " found at index 1")
        count += 1
    if letter == word[2]:
        print(letter + " found at index 2")
        count += 1
    if letter == word[3]:
        print(letter + " found at index 3")
        count += 1
    if letter == word[4]:
        print(letter + " found at index 4")
        count += 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print(
            "1 instance of " + letter + " found in " + word
        )  # different instance because 1 isn't plural
    else:
        print(
            str(count) + " instances of " + letter + " found in " + word
        )  # count is int but must be str


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


# how to import code for use in the REPL:
# from exercises.ex02_chardle import function_name
# must be done in the REPL before running function

if __name__ == "__main__":
    main()

# enables running of code in the terminal
