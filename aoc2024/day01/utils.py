
import ibis
from ibis import _

import aoc2024.utils


def read_data(con: ibis.BaseBackend, filename: str = "input.txt") -> ibis.Table:
    INPUT_TXT = aoc2024.utils.get_filepath("aoc2024.data.day01", filename)
    t = con.read_csv(INPUT_TXT, header=False, names=["a"]).mutate(
        a=_.a.split("   ")[0].cast("int"), b=_.a.split("   ")[1].cast("int")
    )
    return t
