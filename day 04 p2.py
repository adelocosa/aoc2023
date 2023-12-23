from utils import *
from pprint import pprint
from typing import Sequence, TypeAlias, Any
import copy

Card: TypeAlias = dict[str, Any]

test_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def parse_input(input: Sequence[str]) -> list[Card]:
    cards = []
    for line in input:
        card: dict[str, Any] = {"count": 1}
        line = line.split(":")[1][1:].replace("  ", " ")
        winning_numbers_str, my_numbers_str = line.split("|")
        card["winning"] = [int(x) for x in winning_numbers_str.strip(" ").split(" ")]
        card["mine"] = [int(x) for x in my_numbers_str.strip(" ").split(" ")]
        cards.append(card)
    return cards


def iterate_cards(cards: list[Card]) -> list[Card]:
    for i, card in enumerate(cards):
        card_to_add = 1
        for number in card["winning"]:
            if number in card["mine"]:
                cards[i + card_to_add]["count"] += card["count"]
                card_to_add += 1
    return cards


def solve(test: bool) -> int:
    if test:
        input = test_input.split("\n")
    else:
        input = get_input(day=4)
    cards = parse_input(input)
    cards = iterate_cards(cards)
    total_cards = 0
    for card in cards:
        total_cards += card["count"]
    return total_cards


answer = solve(test=False)
print(answer)
