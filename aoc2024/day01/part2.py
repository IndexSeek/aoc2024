import ibis
from ibis import _

from aoc2024.day01.utils import read_data


def solve(con: ibis.BaseBackend, filepath: str = "input.txt") -> int:
    t = read_data(con, filepath)
    t1 = t.select("a")
    t2 = t.select("b").group_by("b").aggregate(counted=_.b.count())
    return int(
        t1.join(t2, t1.a == t2.b, "inner")
        .aggregate(result=(_.a * _.counted).sum())
        .execute()
        .result[0]
    )


if __name__ == "__main__":
    con = ibis.connect("duckdb://")
    print(solve(con, "input.txt"))
