from utils import *
from pprint import pprint
from typing import Sequence, TypeAlias

Point: TypeAlias = tuple[int, int]

test_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def parse_input(input: Sequence[str]) -> tuple[list[tuple[str, Point]], set[Point]]:
    numbers: list[tuple[str, Point]] = []
    gears: set[Point] = set()
    for y, line in enumerate(input):
        number = ""
        startpos = None
        for x, character in enumerate(line):
            if character.isdigit():
                if startpos == None:
                    startpos = x
                    number += character
                else:
                    number += character
            else:
                if character == "*":
                    gears.add((x, y))
                if startpos != None:
                    numbers.append((number, (startpos, y)))
                    number = ""
                    startpos = None
        if startpos != None:
            numbers.append((number, (startpos, y)))

    return numbers, gears


def get_adjacent_points(number: str, origin: Point) -> set[Point]:
    points: set[Point] = set()
    for i in range(len(number)):
        points.add((origin[0] + i + 1, origin[1]))
        points.add((origin[0] + i + -1, origin[1]))
        points.add((origin[0] + i + 1, origin[1] + 1))
        points.add((origin[0] + i - 1, origin[1] + 1))
        points.add((origin[0] + i + 1, origin[1] - 1))
        points.add((origin[0] + i - 1, origin[1] - 1))
        points.add((origin[0] + i, origin[1] + 1))
        points.add((origin[0] + i, origin[1] - 1))
    return points


def get_gear_ratio(numbers: list[tuple[str, Point]], gear: Point) -> int:
    matches = []
    for number in numbers:
        if gear in get_adjacent_points(number[0], number[1]):
            matches.append(int(number[0]))
    if len(matches) == 2:
        return matches[0] * matches[1]
    return 0


def solve(test: bool) -> int:
    if test:
        input = test_input.split("\n")
    else:
        input = get_input(day=3)
    numbers, gears = parse_input(input)
    gear_ratios = 0
    for gear in gears:
        gear_ratios += get_gear_ratio(numbers, gear)
    return gear_ratios


answer = solve(test=False)
print(answer)
