"""This exercise is to plan a tea party, which will help me understand functions."""

__author__: str = "730750473"


def main_planner(guests: int) -> None:
    """This function calls each of the following functions at once."""
    print("A cozy tea party for " + str(guests) + " people!")
    print("Tea bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


# return type None gives a lot more freedom
# converting function calls to strings enables better-looking outputs
# line 11 ~ tea_bags(guests) = tea_count AND treats(guests) = treat_count


def tea_bags(people: int) -> int:
    """This function declares the number of people at the tea party."""
    return people * 2


# there are 2 tea bags per guest, so multiply people by 2 in return statement


def treats(people: int) -> int:
    """This function helps find the number of treats based on teas expected."""
    return int((tea_bags(people)) * 1.5)


# put 1.5 outside of the tea_bags parentheses because that function uses int
# then convert the resulting float to an int


def cost(tea_count: int, treat_count: int) -> float:
    """This function finds the price of tea and treats."""
    return 0.50 * tea_count + 0.75 * treat_count


# counts are not the prices but the number of items
# don't worry about the dollar sign until the main_planner function


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
