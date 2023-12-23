from utils import *
from pprint import pprint
from typing import Sequence, TypeAlias
import copy

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


def parse_input(input: Sequence[str]) -> tuple[list[list[int]], list[Map]]:
    seeds = [int(x) for x in input[0].split(":")[1][1:].split()][::2]
    ranges = [int(x) for x in input[0].split(":")[1][1:].split()][1::2]
    seed_ranges = [[seeds[x], ranges[x]] for x in range(len(seeds))]
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
    return seed_ranges, maps


def map_seed_ranges(map: Map, seeds: list[list[int]]) -> list[list[int]]:
    new_seeds: list[list[int]] = []
    # sort map lines to ensure catching the split seeds
    map.sort(key=lambda x: x["src"])
    for line in map:
        for seed in copy.deepcopy(seeds):
            bottom = seed[0]
            top = seed[0] + seed[1] - 1
            # if any part of the seed is in the map range
            if bottom >= line["src"] and bottom <= (line["src"] + (line["range"] - 1)):
                new_seed = [(bottom - line["src"]) + line["dest"]]
                # split the seed where it exits the map range
                if top > (line["src"] + (line["range"] - 1)):
                    # modify the seed to represent the outer range
                    i = seeds.index(seed)
                    seeds[i][0] = line["src"] + line["range"]
                    seeds[i][1] = top - seeds[i][0] + 1
                    new_seed.append((line["src"] + (line["range"])) - bottom)
                else:  # if the entire seed fits within the range
                    new_seed.append(seed[1])
                    seeds.remove(seed)
                new_seeds.append(new_seed)
    new_seeds.extend(seeds)
    return new_seeds


def solve(test: bool) -> int:
    if test:
        input = test_input.split("\n")
    else:
        input = get_input(day=5)
    seeds, maps = parse_input(input)
    for map in maps:
        seeds = map_seed_ranges(map, seeds)
    return min(x[0] for x in seeds)


answer = solve(test=False)
print(answer)
