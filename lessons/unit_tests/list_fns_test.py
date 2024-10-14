from lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first


# desired behavior and return value
def test_get_first() -> None:
    """get_first should return the first element"""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    assert get_first(dog_breeds) == "husky"


# desired return value
def test_remove_first_return_value() -> None:
    """remove_first should return None"""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    assert remove_first(dog_breeds) == None


# desired behavior
def test_remove_first_behavior() -> None:
    """remove_first should remove the first value from the input"""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    remove_first(dog_breeds)
    assert dog_breeds == ["golden", "poodle", "lab"]


def test_get_first_edge_case() -> None:
    """get_first called on an empty list should return an empty string"""
    assert get_first([]) == ""
