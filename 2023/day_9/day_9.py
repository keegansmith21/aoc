def fmt(input):
    lines = []
    for l in input:
        lines.append([int(i) for i in l.split(" ")])
    return lines


def expand_history_1(h):
    expanded = [h.copy()]
    while True:
        new_line = []
        for i, v in enumerate(expanded[-1][1:]):
            new_line.append(v - expanded[-1][i])
        expanded.append(new_line)
        if set(new_line) == set([0]):
            break
    return expanded


def next_in_sequence_1(expanded):
    expanded[-1].append(0)
    expanded = expanded[::-1]
    for i, e in enumerate(expanded[1:]):
        n = e[-1] + expanded[i][-1]
        expanded[i + 1].append(n)
    return expanded[-1][-1]


def next_in_sequence_2(expanded):
    expanded[-1].insert(0, 0)
    expanded = expanded[::-1]
    for i, e in enumerate(expanded[1:]):
        n = e[0] - expanded[i][0]
        expanded[i + 1].insert(0, n)
    return expanded[-1][0]


def main_1(input):
    hs = fmt(input)
    next_ns = []
    for h in hs:
        expanded = expand_history_1(h)
        next_ns.append(next_in_sequence_1(expanded))

    answer = sum(next_ns)
    print(f"PT 1 ANSWER: {answer}")
    pass


def main_2(input):
    hs = fmt(input)
    next_ns = []
    for h in hs:
        expanded = expand_history_1(h)
        next_ns.append(next_in_sequence_2(expanded))

    answer = sum(next_ns)
    print(f"PT 1 ANSWER: {answer}")
    pass


if __name__ == "__main__":
    with open("2023/day_9/input.txt", "r") as f:
        input = f.readlines()
    # main_1(input)
    main_2(input)
