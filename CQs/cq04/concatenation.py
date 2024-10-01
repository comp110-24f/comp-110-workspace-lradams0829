"""CQ04 concatenation file"""

__author__ = "730750473"


def concat(str1: str, str2: str) -> str:
    return str1 + str2


# use return and not print for concat because there's a return type up top

if __name__ == "__main__":
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(str1=word1, str2=word2))

# use 'if __name__ == "__main__":' in order to prevent stuff below importing
