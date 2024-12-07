import ibis
from ibis import _

from aoc2024.day01.utils import read_data


def solve(con: ibis.BaseBackend, filepath: str = "input.txt") -> int:
    t = read_data(con, filepath)
    t1 = t.select("a").mutate(row_num=ibis.row_number().over(order_by="a"))
    t2 = t.select("b").mutate(row_num=ibis.row_number().over(order_by="b"))
    return (
        t1.join(t2, ["row_num"])
        .mutate(diff=(_.a - _.b).abs())
        .diff.sum()
        .to_pyarrow()
        .as_py()
    )


if __name__ == "__main__":
    con = ibis.connect("duckdb://")
    print(solve(con, "input.txt"))
