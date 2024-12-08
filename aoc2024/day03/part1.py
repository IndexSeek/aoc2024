import re

from aoc2024.day03.utils import read_data


def solve(filepath: str = "input.txt") -> int:
    data = read_data(filepath)
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, data)
    return sum(int(x) * int(y) for x, y in matches)


if __name__ == "__main__":
    print(solve("input.txt"))
