from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a str representation of a linked list."""
        rest: str = "TO_DO"
        # TO_DO: Figure out the rest of the list
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))
print(one)
print(str(courses))
print(courses)


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


print(to_str(one))
print(to_str(courses))


def last(head: Node) -> int:
    """Return the last value of a non-empty list"""
    # base case: when head is the last node
    #   return its value
    # recursive case: figure out the last node (recursive call) in "rest of the list"
    #   return this value
    print(f"Enter last {head.value}")
    if head.next is None:
        print(f"Return base case: {head.value}")
        return head.value
    else:
        rest: int = last(head.next)
        print(f"Return recur: {head.value} -> {rest}")
        return rest


print(last(one))  # Expect to print 2
print(last(courses))  # Expect to print 301


def recursive_range(start: int, end: int) -> Node | None:
    """Build a list recursively from start to end."""
    if start > end:
        raise ValueError("invalid arguments")
    elif start == end:
        # base case
        return None
    else:
        # recrusive case
        # STEP 1: handle the first value in the new list
        first: int = start
        # STEP 2: let the rest of the list be handled recursively
        rest: Node | None = recursive_range(start + 1, end)
        return Node(first, rest)
        # same as 'return Node(start, recursive_range(start + 1, end))'


three: Node | None = recursive_range(110, 113)
print(three)
