from utils import *
from pprint import pprint
from typing import Sequence, TypeAlias

Map: TypeAlias = list[dict[str, int]]

test_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def parse_input(input: Sequence[str]) -> tuple[list[int], list[Map]]:
    seeds = [int(x) for x in input[0].split(":")[1][1:].split()]
    maps: list[Map] = []
    found = False
    new_map = []
    for line in input:
        if not line:
            found = False
            if new_map:
                maps.append(new_map)
            new_map = []
        if found:
            new_map.append(
                {
                    "dest": int(line.split()[0]),
                    "src": int(line.split()[1]),
                    "range": int(line.split()[2]),
                }
            )
        if "map" in line:
            found = True
    maps.append(new_map)
    return seeds, maps


def map_seed(seed: int, maps: list[Map]) -> int:
    for map in maps:
        for line in map:
            if seed >= line["src"] and seed <= (line["src"] + line["range"]):
                seed = (seed - line["src"]) + line["dest"]
                break
    return seed


def solve(test: bool) -> int:
    if test:
        input = test_input.split("\n")
    else:
        input = get_input(day=5)
    seeds, maps = parse_input(input)
    locations = []
    for seed in seeds:
        locations.append(map_seed(seed, maps))
    return min(locations)


answer = solve(test=False)
print(answer)
