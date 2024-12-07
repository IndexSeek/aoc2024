import ibis
import polars as pl
from ibis import _

from aoc2024.day02.utils import read_data


def solve(filepath: str = "input.txt") -> int:
    df = read_data(filepath)
    diff_expr = pl.col("a").list.diff(null_behavior="drop")

    return (
        df.select(a=pl.col("a").str.split(" ").cast(pl.List(pl.Int64)))
        .with_columns(
            is_sorted=(
                (pl.col("a") == pl.col("a").list.sort())
                | (pl.col("a") == pl.col("a").list.sort(descending=True))
            ).alias("is_sorted")
        )
        .with_columns(
            min_diff=diff_expr.list.min().abs(), max_diff=diff_expr.list.max().abs()
        )
        .filter(
            pl.col("is_sorted"),
            (pl.col("min_diff").is_between(1, 3) & pl.col("max_diff").is_between(1, 3)),
        )
        .select(pl.len())
        .to_arrow()
        .to_pydict()
        .get("len")[0]
    )


if __name__ == "__main__":
    print(solve("input.txt"))
