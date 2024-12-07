from aoc2024.day01 import part1, part2


def test_part1(con):
    assert part1.solve(con, "input_test.txt") == 11


def test_part2(con):
    assert part2.solve(con, "input_test.txt") == 31
