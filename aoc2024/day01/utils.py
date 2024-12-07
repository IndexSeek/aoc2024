import os

import ibis
from ibis import _


def read_data(con: ibis.BaseBackend, filepath: str = "input.txt") -> ibis.Table:
    INPUT_TXT = os.path.join(os.path.dirname(__file__), filepath)
    t = con.read_csv(INPUT_TXT, header=False, names=["a"]).mutate(
        a=_.a.split("   ")[0].cast("int"), b=_.a.split("   ")[1].cast("int")
    )
    return t
