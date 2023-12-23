from utils import *
from pprint import pprint
from typing import Sequence

test_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

bag_contents = {"red": 12, "green": 13, "blue": 14}


def parse_games(input: Sequence[str]) -> list[list[dict[str, int]]]:
    games = []
    for line in input:
        line = line.split(":")[1][1:]
        steps = [x.replace(",", "").lstrip(" ") for x in line.split(";")]
        game = []
        for step_str in steps:
            ball_counts = step_str.split()[::2]
            ball_colors = step_str.split()[1::2]
            step = {}
            for i, color in enumerate(ball_colors):
                step[color] = int(ball_counts[i])
            game.append(step)
        games.append(game)
    return games


def is_possible(game: list[dict[str, int]]) -> bool:
    for step in game:
        for color, amount in step.items():
            if bag_contents[color] < amount:
                return False
    return True


def solve(test: bool) -> int:
    if test:
        input = test_input.split("\n")
    else:
        input = get_input(2)
    games = parse_games(input)
    total = 0
    for i, game in enumerate(games):
        if is_possible(game):
            total += i + 1
    return total


answer = solve(test=False)
print(answer)
