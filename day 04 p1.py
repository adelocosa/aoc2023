from utils import *
from pprint import pprint
from typing import Sequence

test_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def parse_input(input: Sequence[str]) -> list[tuple[list[int], list[int]]]:
    cards = []
    for line in input:
        line = line.split(":")[1][1:].replace("  ", " ")
        winning_numbers_str, my_numbers_str = line.split("|")
        winning_numbers = [int(x) for x in winning_numbers_str.strip(" ").split(" ")]
        my_numbers = [int(x) for x in my_numbers_str.strip(" ").split(" ")]
        cards.append((winning_numbers, my_numbers))
    return cards


def solve(test: bool) -> int:
    if test:
        input = test_input.split("\n")
    else:
        input = get_input(day=4)
    cards = parse_input(input)
    total_points = 0
    for card in cards:
        points = 0
        for number in card[0]:
            if number in card[1]:
                if not points:
                    points += 1
                else:
                    points *= 2
        total_points += points
    return total_points


answer = solve(test=False)
print(answer)
