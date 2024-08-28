"""My first challenge question in COMP 110!"""

__author__ = "730750473"


def mimic(message: str) -> str:
    """This function takes the input and repeats it back..."""
    return message


def main() -> None:
    """prints the result of calling mimic"""
    print(mimic(message=input("What is your message?")))
    return None


if __name__ == "__main__":
    main()
