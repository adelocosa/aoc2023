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
    symbols: set[Point] = set()
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
                if character != ".":
                    symbols.add((x, y))
                if startpos != None:
                    numbers.append((number, (startpos, y)))
                    number = ""
                    startpos = None
        if startpos != None:
            numbers.append((number, (startpos, y)))

    return numbers, symbols


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


def is_part_number(adjacent: set[Point], symbols: set[Point]) -> bool:
    for symbol in symbols:
        if symbol in adjacent:
            return True
    return False


def solve(test: bool) -> int:
    if test:
        input = test_input.split("\n")
    else:
        input = get_input(day=3)
    numbers, symbols = parse_input(input)
    part_numbers = []
    for number in numbers:
        adjacent = get_adjacent_points(number[0], number[1])
        if is_part_number(adjacent, symbols):
            part_numbers.append(int(number[0]))
    print(part_numbers)
    return sum(part_numbers)


answer = solve(test=False)
print(answer)
