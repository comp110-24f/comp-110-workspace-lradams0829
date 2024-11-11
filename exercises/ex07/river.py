"""File to define River class."""

__author__: str = "730750473"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """River class with attributes day, fish, and bears"""

    day: int  # day of river's lifecycle that is modeled
    fish: list[Fish]  # stores fish population
    bears: list[Bear]  # stores bear population

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """fish and bears added to survival lists if not too old"""
        surviving_fish: list[Fish] = []
        for elem in self.fish:  # elem accesses item in list of Fish
            if elem.age <= 3:
                # from there, attributes and method definitions can be accessed
                surviving_fish.append(elem)
            self.fish = surviving_fish
        surviving_bears: list[Bear] = []
        for elem in self.bears:
            if elem.age <= 5:
                surviving_bears.append(elem)
            self.bears = surviving_bears

    def remove_fish(self, amount: int) -> None:
        """removes fish from the river"""
        if amount > len(self.fish):
            self.fish = []  # clears pond of fish with no error
        else:
            for _ in range(0, amount):  # _ acts as placeholder
                self.fish.pop(0)  # first element is popped always

    def bears_eating(self) -> None:
        """remove 3 in 5 fish for bear consumption"""
        if len(self.fish) >= 5:  # more efficient with if statement before for loop
            for elem in self.bears:  # assuming first bear gets the fish
                self.remove_fish(3)
                elem.eat(3)
        else:
            for elem in self.bears:
                self.remove_fish(0)
                elem.eat(0)

    def check_hunger(self) -> None:
        """add bears that don't go hungry to surviving list"""
        surviving_bears: list[Bear] = []
        for elem in self.bears:
            if elem.hunger_score >= 0:
                surviving_bears.append(elem)
                self.bears = surviving_bears

    def repopulate_fish(self) -> None:
        """every pair of fish has 4 offspring, a single fish cannot reproduce"""
        for _ in range((len(self.fish) // 2) * 4):
            # floor division returns the quotient but no remainder
            self.fish.append(Fish())

    def repopulate_bears(self) -> None:
        """every pair of bears has 1 offspring, a single bear cannot reproduce"""
        for _ in range((len(self.bears) // 2)):
            self.bears.append(Bear())

    def view_river(self) -> None:
        """implements a nice format during class call"""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """simulate one week of life in the river"""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
