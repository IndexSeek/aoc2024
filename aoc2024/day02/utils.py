import os

import ibis
import polars as pl
from ibis import _


def read_data(filepath: str = "input.txt") -> pl.DataFrame:
    INPUT_TXT = os.path.join(os.path.dirname(__file__), filepath)
    df = pl.read_csv(INPUT_TXT, has_header=False, new_columns=["a"])
    return df
