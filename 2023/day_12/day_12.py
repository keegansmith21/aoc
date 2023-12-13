import re
from functools import cache
from itertools import combinations

GROUP_MATHING_REGEX_DOTS = re.compile(r"(?:(?<=^)|(?<=\.))#+(?=\.|$)")


def fmt(input):
    lines = []
    groups = []
    for l in input:
        lines.append(list(l.strip().split(" ")[0]))
        g = l.strip().split(" ")[1].split(",")
        groups.append([int(i) for i in g])
    return lines, groups


def line_groups(line):
    _line = "".join(line)
    groups = re.findall(GROUP_MATHING_REGEX_DOTS, _line)
    groups = [len(list(i)) for i in groups]
    return groups


def replace_elements(line, p, locs):
    for el, loc in zip(p, locs):
        line[loc] = el
    return tuple(line)


def replace_with_hashes(size, count):
    for positions in combinations(range(size), count):
        p = ["."] * size

        for i in positions:
            p[i] = "#"
        yield (p)


def main_1(input):
    lines, groups = fmt(input)
    arrangements = 0
    for line, group in zip(lines, groups):
        qs = line.count("?")
        required_hashes = sum(group) - line.count("#")
        pos = list(replace_with_hashes(qs, required_hashes))
        print(len(pos))

        q_locs = []
        for i, l in enumerate(line):
            if l == "?":
                q_locs.append(i)
        for p in pos:
            _line = replace_elements(line.copy(), p, q_locs)
            if line_groups(_line) == group:
                arrangements += 1

    print(f"PT 1 ANSWER: {arrangements}")


def main_2(input):
    lines, groups = fmt(input)

    new_lines = []
    new_groups = []
    for l, g in zip(lines, groups):
        new_lines.append(l * 5)
        new_groups.append(g * 5)

    arrangements = 0
    for line, group in zip(new_lines, new_groups):
        qs = line.count("?")
        required_hashes = sum(group) - line.count("#")
        print(arrangements)
        pos = replace_with_hashes(qs, required_hashes)

        q_locs = []
        for i, l in enumerate(line):
            if l == "?":
                q_locs.append(i)
        for p in pos:
            _line = replace_elements(line.copy(), p, q_locs)
            if line_groups(_line) == group:
                arrangements += 1
    print(f"PT 2 ANSWER: {arrangements}")


if __name__ == "__main__":
    with open("2023/day_12/input.txt", "r") as f:
        input = f.readlines()
    main_1(input)
    main_2(input)
