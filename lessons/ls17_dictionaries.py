"""Examples of dictionary syntax with Ice Cream Shop order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# add key value entry by directly assigning to a key
ice_cream["mint"] = 3

# test if pbj is a key in ice_cream
has_pbj: bool = "pbj" in ice_cream

# to remove, we use the pop method and input a key
ice_cream.pop("strawberry")

# to iterate over every key, use for-in loop
for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor} has {tally} orders")
