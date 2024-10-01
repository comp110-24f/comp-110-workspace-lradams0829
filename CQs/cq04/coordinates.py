"""CQ04 coordinates file"""

__author__ = "730750473"


def get_coords(xs: str, ys: str) -> None:
    x_index: int = 0
    while x_index < len(xs):
        y_index: int = 0
        while y_index < len(ys):
            print("(" + xs[x_index] + "," + ys[y_index] + ")")
            y_index += 1
        x_index += 1


# don't use return because the return type up top is None
# extra strings in print call due to (x,y) notation
