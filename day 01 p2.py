from utils import *

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

test_input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


def parse_line(line: str) -> list[str]:
    parsed = []
    for i, character in enumerate(line):
        if character.isdigit():
            parsed.append(character)
            continue
        for j, number in enumerate(numbers):
            if line[i : i + len(number)] == number:
                parsed.append(str(j + 1))
    return parsed


values = []
for line in get_input(1):
    parsed = parse_line(line)
    values.append(int(parsed[0] + parsed[-1]))

answer = sum(values)
print(answer)
