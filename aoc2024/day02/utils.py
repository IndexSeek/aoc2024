import os

import ibis
import polars as pl
from ibis import _

import importlib.resources as resources


def read_data(filepath: str = "input.txt") -> pl.DataFrame:
    INPUT_TXT = resources.files("aoc2024.data.day02").joinpath(filepath)
    df = pl.read_csv(INPUT_TXT, has_header=False, new_columns=["a"])
    return df
