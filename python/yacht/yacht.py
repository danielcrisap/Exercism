"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

MULTIPLIABLE = [
    ONES,
    TWOS,
    THREES,
    FOURS,
    FIVES,
    SIXES
]

LITTLE_STRAIGHT_DICE = [1, 2, 3, 4, 5]
BIG_STRAIGHT_DICE = [2, 3, 4, 5, 6]


def score(dice, category):
    dice.sort()
    result = 0
    max_equal = max(dice, key=dice.count)
    min_equal = min(dice, key=dice.count)

    if category in MULTIPLIABLE:
        result = dice.count(category) * category

    if category is CHOICE:
        result = sum(dice)

    if category is YACHT:
        if dice.count(5) == len(dice):
            result = 50

    if category is FULL_HOUSE:
        if(
            dice.count(max_equal) == 3
            and dice.count(min_equal) == 2
        ):
            result = sum(dice)

    if category is FOUR_OF_A_KIND:
        if dice.count(max_equal) >= 4:
            result = max_equal * 4

    if category is LITTLE_STRAIGHT:
        if dice == LITTLE_STRAIGHT_DICE:
            result = 30

    if category is BIG_STRAIGHT:
        if dice == BIG_STRAIGHT_DICE:
            result = 30

    return result
