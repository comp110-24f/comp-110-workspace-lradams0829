def count_regs(county: str, all_counties: list[str]) -> int:
    """count number of people who are registered in a specific county"""
    tally: int = 0
    for elem in all_counties:
        if elem == county:
            tally += 1
    return tally
