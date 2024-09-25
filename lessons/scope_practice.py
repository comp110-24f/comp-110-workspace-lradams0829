"""Some scope examples:"""


def remove_chars(msg: str, char: str) -> str:
    """Return a copy of message with all instances of char removed."""
    copy: str = ""
    index: int = 0
    while index <= len(msg):
        if msg[index] != char:  # if the character is NOT char
            copy += msg[index]  # add it to copy
        index += 1
    return copy


# print(remove_chars(msg="football", char="o"))

# create a variable called word with the value "yoyo"
word: str = "yoyo"  # global variable
# print the result of calling the function with arguments word and "y"
print(remove_chars(msg=word, char="y"))  # with keyword arguments
# print the result of calling the function with arguments word and "o"
print(remove_chars(word, "o"))  # with positional arguments
