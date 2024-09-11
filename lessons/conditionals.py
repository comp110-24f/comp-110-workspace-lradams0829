"""Practice with conditionals."""


def less_than_10(num: int) -> None:
    """Tell me if num is < 10."""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("Wow!")


# less_than_10(num=5)


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


# print(check_first_letter(word="happy", letter="h"))
# print(check_first_letter(word="happy", letter="s"))


def get_weather_report() -> str:
    """Display weather advice."""
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


# get_weather_report()
