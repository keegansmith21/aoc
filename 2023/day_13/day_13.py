from itertools import product

from lib.aoc import transpose_list_of_lists


def fmt(input):
    chunks = []
    chunk = []
    for l in input:
        if l == "\n":
            chunks.append(chunk)
            chunk = []
        else:
            chunk.append(list(l.strip()))
    chunks.append(chunk)  # Last chunk
    return chunks


def get_row_reflection(row):
    # Find where a row's left side is equal to its right side
    r = []

    # look left to right
    for i in range(1, len(row)):
        left_side = row[:i]
        right_side = row[i:]
        if len(left_side) < len(right_side):
            right_side = right_side[: len(left_side)]
        elif len(right_side) < len(left_side):
            left_side = left_side[i - len(right_side) :]

        if list(reversed(right_side)) == left_side:
            r.append(i)
    return r


def chunk_value(chunk):
    column_reflections = []
    row_reflections = []
    for i in chunk:
        column_reflections.append(get_row_reflection(i))
    for i in transpose_list_of_lists(chunk):
        row_reflections.append(get_row_reflection(i))
    col = set.intersection(*[set(i) for i in column_reflections])
    row = set.intersection(*[set(i) for i in row_reflections])
    if list(col):
        return (list(col)[0], None)
    elif list(row):
        return (None, list(row)[0])
    else:
        return (None, None)


def chunk_value_2(chunk):
    column_reflections = []
    row_reflections = []
    for i in chunk:
        column_reflections.append(get_row_reflection(i))
    col_counts = []
    for i, _ in enumerate(chunk):
        c = 0
        for j in column_reflections:
            if i in j:
                c += 1
        col_counts.append(c)
    if len(chunk[0]) - 1 in col_counts:
        return col_counts.index(len(chunk) - 1), None

    for i in transpose_list_of_lists(chunk):
        row_reflections.append(get_row_reflection(i))
    row_counts = []
    for i, _ in enumerate(chunk[0]):
        c = 0
        for j in row_reflections:
            if i in j:
                c += 1
        row_counts.append(c)
    if len(chunk) - 1 in row_counts:
        return None, row_counts.index(len(chunk[0]) - 1)


def main_1(input):
    chunks = fmt(input)
    answer = 0
    for chunk in chunks:
        val = chunk_value(chunk)
        if val[0]:
            answer += val[0]
        elif val[1]:
            answer += val[1] * 100

    print(f"PT 1 ANSWER: {answer}")


def main_2(input):
    chunks = fmt(input)
    answer = 0
    for chunk in chunks:
        val = chunk_value_2(chunk)
        if val[0]:
            answer += val[0]
        elif val[1]:
            answer += val[1] * 100

    # for chunk in chunks:
    #     original_ref = chunk_value(chunk)
    #     for i, j in product(range(len(chunk)), range(len(chunk[0]))):
    #         chunk[i][j] = "#" if chunk[i][j] == "." else "."
    #         new_ref = chunk_value(chunk)
    #         if new_ref == original_ref:
    #             chunk[i][j] = "#" if chunk[i][j] == "." else "."
    #             continue
    #         if new_ref[0] and new_ref[1]:
    #             chunk[i][j] = "#" if chunk[i][j] == "." else "."
    #             continue
    #         elif new_ref[0]:
    #             answer += new_ref[0]
    #             break
    #         elif new_ref[1]:
    #             answer += new_ref[1] * 100
    #             break
    #         chunk[i][j] = "#" if chunk[i][j] == "." else "."
    #     else:
    #         print("no")

    print(f"PT 2 ANSWER: {answer}")


if __name__ == "__main__":
    with open("2023/day_13/input.txt", "r") as f:
        input = f.readlines()
    main_1(input)
    main_2(input)
