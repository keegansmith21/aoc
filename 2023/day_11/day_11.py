from lib.aoc import n_in_range


def fmt(input):
    fmtd = []
    for l in input:
        fmtd.append(list(l.strip()))
    return fmtd


def is_that_need_expanding(g_map):
    rows_to_expand = []
    for i, r in enumerate(g_map):
        if set(r) == set(["."]):
            rows_to_expand.append(i)

    cols_to_expand = []
    row_col_swap = list(map(list, zip(*g_map)))
    for i, c in enumerate(row_col_swap):
        if set(c) == set(["."]):
            cols_to_expand.append(i)
    return rows_to_expand, cols_to_expand


def expand_g_map(g_map):
    expanded_g_map = g_map.copy()
    rows_to_expand, cols_to_expand = is_that_need_expanding(expanded_g_map)

    for r in sorted(rows_to_expand, reverse=True):
        expanded_g_map.insert(r, ["." for _ in range(len(expanded_g_map[0]))])

    for c in sorted(cols_to_expand, reverse=True):
        for r in expanded_g_map:
            r.insert(c, ".")

    return expanded_g_map


def shortest_d(c1, c2):
    # Gets the shortest distance in steps between two points
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])


def shortest_d_2(c1, c2, ex_r, ex_c):
    crosses = 0

    r_range = (c1[0], c2[0])
    for r in ex_r:
        if n_in_range(r, r_range, inclusive=(False, False)):
            crosses += 1

    c_range = (c1[1], c2[1])
    for c in ex_c:
        if n_in_range(c, c_range, inclusive=(False, False)):
            crosses += 1

    shortest = shortest_d(c1, c2)
    shortest += crosses * int(1e6 - 1)

    return shortest


def shortest_distances(g_map):
    galaxies = []
    for j, r in enumerate(g_map):
        for i, c in enumerate(r):
            if c == "#":
                galaxies.append((j, i))

    dists = []
    for g1 in galaxies:
        for g2 in galaxies:
            dists.append(shortest_d(g1, g2))

    return dists


def shortest_distances_2(g_map):
    ex_r, ex_c = is_that_need_expanding(g_map)

    galaxies = []
    for j, r in enumerate(g_map):
        for i, c in enumerate(r):
            if c == "#":
                galaxies.append((j, i))

    pairs = []
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            pair = (galaxies[i], galaxies[j])
            pairs.append(pair)

    dists = []
    for g1, g2 in pairs:
        dists.append(shortest_d_2(g1, g2, ex_r, ex_c))

    return dists


def main_1(input):
    g_map = fmt(input)
    expanded_g_map = expand_g_map(g_map)
    dists = shortest_distances(expanded_g_map)
    answer = sum(dists) // 2
    print(f"PT 1 ANSWER: {answer}")


def main_2(input):
    g_map = fmt(input)
    dists = shortest_distances_2(g_map)
    answer = sum(dists)
    print(f"PT 2 ANSWER: {answer}")


if __name__ == "__main__":
    with open("2023/day_11/input.txt", "r") as f:
        input = f.readlines()
    main_1(input)
    main_2(input)
