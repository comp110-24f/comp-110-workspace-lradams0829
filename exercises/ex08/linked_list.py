"""ex08, Linked Lists!"""

from __future__ import annotations

__author__: str = "730750473"


class Node:
    """Backbone class definition."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Constructor method definition."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a str representation of a Linked List."""
        rest: str = ""
        # "": figure out the rest of the list
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


def value_at(head: Node | None, index: int) -> int:
    """Returns the value of a Node at the given index of the Linked List."""
    if head is None:  # edge case
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:  # base case
        return head.value
    else:  # recursive case
        return value_at(head.next, index - 1)
    # head.next enables movement through Linked List
    # make index smaller each call to get closer to base case
    # example:
    # value_at(Node(10, Node(20, Node(30, None))), 2)
    # if index != 0, go to next Node and subtract index by 1, repeat until index == 0
    # the first head.value is 10, but the index isn't 0 (it's 2)
    # the second head.value is 20, but the index isn't 0 (it's 1)
    # the third head.value is 30, and the index is 0


def max(head: Node | None) -> int:
    """Returns the maximum value of the Linked List."""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:  # base case
        return head.value
    # if head.next is None, its the last Node in the Linked List
    max_of_rest: int = max(head.next)  # find maximum in the rest of the Linked List
    # compare current Node value with maximum of the rest of the Linked List
    if head.value >= max_of_rest:  # recursive case
        return head.value
    else:
        return max_of_rest


# this is using a for-in loop instead :(
# def linkify(items: list[int]) -> Node | None:
# """Returns a Linked List of Nodes with the values of items."""
# if items == []:
#     return None
# create head:
# head: Node | None = Node(items[0], None)  # head value is first list element
# set a current Node to iterate with
# present_node: Node | None = head
# iterate through rest of the Linked List:
# for element in items[1:]:  # start at second element, iterate through last element
#     new_node: Node | None = Node(element, None)
# make the next of head into a new Node:
#     present_node.next = new_node
# make the new Node into the new present Node:
#     present_node = new_node
# return print(head)  # print head so that linkify evaluates in the REPL


def linkify(items: list[int]) -> Node | None:
    """Returns a Linked List of Nodes with the values of list items."""
    if items == []:  # edge case
        return None
    # items[0] serves as a base case for the rest
    # rest is linkify(items[1:]), recursive case
    # items[1:] goes from second item until end of list
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns a Linked List of Nodes with values of list items multiples by factor."""
    if head is None:  # base case
        return None
    # first part of return should be first element * factor
    start: int = head.value * factor
    # move to next Node and repeat
    return Node(start, scale(head.next, factor))
