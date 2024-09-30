"""Understanding lists and associated syntax!"""

# my_numbers: list[float] = []  # LITERAL
# my_numbers: list[float] = list()  # CONSTRUCTOR

# my_numbers.append(1.5)
# my_numbers.append(2.3)
# print(my_numbers)

# ANALOGY ~
# my_name: str = "" # LITERAL
# my_name: str = str() # CONSTRUCTOR

# CREATING POPULATED LIST, SUBSCRIPTION NOTATION/INDEXING, MODIFYING BY INDEX ~
game_points: list[int] = [102, 86, 94]
# print(game_points)
# game_points[1] = 72
# print(game_points)
# print(game_points[2])
# print(len(game_points))

# LISTS ARE MUTABLE
# USE len() TO FIND THE NUMBER OF ITEMS IN A LIST
# USE FUNCTION_NAME.pop(INDEX) TO REMOVE ITEMS FROM A LIST

# function name: display
# parameter: list of integers
# RV: None
# print every element in the input list
# call display on game_points


def display(input_list: list[int]) -> None:
    """displays all elements of input_list"""
    index: int = 0
    while index < len(input_list):
        print(input_list[index])
        index += 1


display(input_list=game_points)
