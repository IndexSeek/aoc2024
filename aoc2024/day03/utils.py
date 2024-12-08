import polars as pl

from aoc2024.utils import get_filepath


def read_data(filename: str = "input.txt") -> str:
    with open(get_filepath("aoc2024.data.day03", filename), "r") as f:
        return f.read()
