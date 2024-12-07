import polars as pl

import aoc2024.utils


def read_data(filename: str = "input.txt") -> pl.DataFrame:
    df = pl.read_csv(
        aoc2024.utils.get_filepath("aoc2024.data.day02", filename),
        has_header=False,
        new_columns=["a"],
    )
    return df
