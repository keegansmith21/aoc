from functools import cache
from time import time

from lib import aoc


def fmt(input):
    fmtd = [list(i.strip()) for i in input]
    return fmtd


@cache
def leftify(s):
    os = s.count("O")
    ds = s.count(".")
    return "O" * os + "." * ds


@cache
def shift_left(row):
    newrow = "".join(row).split("#")
    newrow = [leftify(i) for i in newrow]
    return "#".join(newrow)


@cache
def rightify(s):
    os = s.count("O")
    ds = s.count(".")
    return "." * ds + "O" * os


@cache
def shift_right(row):
    newrow = "".join(row).split("#")
    newrow = [rightify(i) for i in newrow]
    return "#".join(newrow)


def main_1(input):
    lines = fmt(input)
    xlines = aoc.transpose_list_of_lists(lines)
    xshifted = []
    for row in xlines:
        xshifted.append(shift_left(tuple(row)))
    shifted = aoc.transpose_list_of_lists(xshifted)

    with open("2023/day_14/part_1.txt", "w") as f:
        for row in shifted:
            f.write("".join(row) + "\n")

    load = 0
    for i, row in enumerate(shifted):
        rocks = row.count("O")
        load += rocks * (len(shifted) - i)

    print(f"PT 1 ANSWER: {load}")


def iteration(lines):
    # North
    lines = aoc.transpose_list_of_lists(lines)
    shifted = []
    for row in lines:
        shifted.append(shift_left(tuple(row)))
    lines = aoc.transpose_list_of_lists(shifted)

    # West
    shifted = []
    for row in lines:
        shifted.append(shift_left(tuple(row)))
    lines = shifted

    # South
    lines = aoc.transpose_list_of_lists(lines)
    shifted = []
    for row in lines:
        shifted.append(shift_right(tuple(row)))
    lines = aoc.transpose_list_of_lists(shifted)

    # East
    shifted = []
    for row in lines:
        shifted.append(shift_right(tuple(row)))
    lines = shifted
    return lines


def main_2(input):
    lines = fmt(input)
    hashes = {}
    for i in range(1000000000):
        lines = iteration(lines)

        this_hash = hash(tuple("".join(l) for l in lines))
        if this_hash in hashes:
            print("!", i, hashes[this_hash])
            s = hashes[this_hash]
            loop_cycle_length = i - s
            n = (1000000000 - (loop_cycle_length + s)) // loop_cycle_length
            r = 1000000000 - (n * loop_cycle_length) - s

            total_iterations_from_start = i + loop_cycle_length
            print(total_iterations_from_start)
            break
        else:
            hashes[this_hash] = i

    for i in range(r):
        lines = iteration(lines)

    with open("2023/day_14/part_2.txt", "w") as f:
        for row in lines:
            f.write("".join(row) + "\n")

    load = 0
    for i, row in enumerate(lines):
        rocks = row.count("O")
        load += rocks * (len(lines) - i)

    print(f"PT 2 ANSWER: {load}")


if __name__ == "__main__":
    with open("2023/day_14/input.txt", "r") as f:
        input = f.readlines()
    # main_1(input)
    main_2(input)
