"""ex06, dictionaries"""

__author__ = "730750473"


def invert(original_dictionary: dict[str, str]) -> dict[str, str]:
    """function inverts key and value for each component of input"""
    new_dictionary: dict[str, str] = {}  # initialize empty dict to add inverted values
    for original_key in original_dictionary:
        # iterates over every key in original_dictionary
        if original_dictionary[original_key] in new_dictionary:
            # checks if value from original_dictionary is already key in new_dictionary
            # cannot invert if duplicate values in original_dictionary
            raise KeyError("cannot have duplicate keys")
        new_dictionary[original_dictionary[original_key]] = original_key
        # assign "original_value" as a key in new_dictionary
        # assign value for new_dictionary to be original_key
    return new_dictionary


def favorite_color(names_and_colors: dict[str, str]) -> str:
    """function returns most popular color from the dictionary"""
    tally: dict[str, int] = {}  # empty dictionary to store colors and their count
    for name in names_and_colors:
        if names_and_colors[name] in tally:
            # names_and_colors[name] = color
            # if color is already in tally:
            tally[names_and_colors[name]] += 1
            # add 1 to tally value
        else:
            tally[names_and_colors[name]] = 1
            # if color not in tally, add it to tally with value of 1
    most_popular = ""  # empty string for answer
    highest_tally = 0
    for key in tally:
        # loop through tally to find highest value (most instances of color)
        if tally[key] > highest_tally:
            # >, for 2 colors with same instances, first color takes precedence
            highest_tally = tally[key]
            most_popular = key
    return most_popular


def count(initial_list: list[str]) -> dict[str, int]:
    """function changes list elements to dictionary keys and # of instances to values"""
    summary_dictionary: dict[str, int] = {}
    # stores elements as keys and count as value
    for element in initial_list:
        if element in summary_dictionary:
            # if list element is already a key in dictionary:
            summary_dictionary[element] += 1
            # increase the value at said key by 1
        else:
            summary_dictionary[element] = 1
            # if element not in count, add it to count with value of 1
    return summary_dictionary


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """function categorizes words into dictionary based on first letter"""
    glossary: dict[str, list[str]] = {}  # initialize dictionary to return later
    for element in words:  # loop over words in list
        first_letter: str = element[0].lower()
        # element[0] is first character of a string and .lower() makes it lowercase
        if first_letter not in glossary:
            # need to make sure first_letter is added to glossary
            glossary[first_letter] = []
            # initialize list that correlates to first_letter
            # exit if block and go to next line (70)
        glossary[first_letter].append(element)
        # line above applies regardless of if statement evaluating to True or False
    return glossary


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """function adds students to attendance dictionary of days and student list"""
    # add lists to dictionary for days that aren't already there
    if day not in attendance:
        attendance[day] = []
    # attendance[day] accesses the list in attendance
    # append adds the student to the list
    # there is no need for a loop because only one student is added at a time
    # MAKE SURE TO PREVENT ADDING MUTIPLE INSTANCES OF SAME NAME WITHIN A DAY
    if student not in attendance[day]:
        # next line not accessed if student already in attendance list
        attendance[day].append(student)
    # no return statement, just mutated dictionary
