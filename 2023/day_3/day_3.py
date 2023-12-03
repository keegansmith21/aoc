import re

NON_ALPHANUMERIC = r"[^a-zA-Z\d\s:.]"
NUMERIC = r"\d+"
GEARS = r"\*"


def find_pattern_indexes(pattern, line):
    matches = re.finditer(pattern, line)
    match_indexes = [(match.start(), match.end()) for match in matches]
    return match_indexes


def transform_input(input, symbols_pattern=NON_ALPHANUMERIC):
    transformed = []
    numbers = []
    symbols = []
    for line in input:
        line = line.strip()
        line_numbers = find_pattern_indexes(NUMERIC, line)
        numbers.append(line_numbers)
        symbol_indexes = find_pattern_indexes(symbols_pattern, line)
        symbols.append(symbol_indexes)
        line = [*line]
        for start, end in symbol_indexes:
            for j in range(start, end):
                line[j] = "T"
        transformed.append(line)
    return transformed, numbers, symbols


def part_verify(line, indices, above_line=None, below_line=None):
    start, end = indices

    left_index = start - 1
    right_index = end + 1
    if left_index < 0:
        left_index = 0
    if right_index >= len(line):
        right_index = len(line) - 1

    neighbours = []
    neighbours.extend(line[left_index:right_index])

    if above_line:
        neighbours.extend(above_line[left_index:right_index])
    if below_line:
        neighbours.extend(below_line[left_index:right_index])

    return bool("T" in neighbours)


def find_part_numbers(input, numbers):
    part_numbers = []
    for row_n, indices in enumerate(numbers):
        line = input[row_n]
        # Get above + below row indexes
        if row_n == 0:
            above_row = None
        else:
            above_row = input[row_n - 1]
        if row_n == len(input) - 1:
            below_row = None
        else:
            below_row = input[row_n + 1]

        for start, end in indices:
            if not part_verify(line, (start, end), above_row, below_row):
                continue
            part_numbers.append(int("".join(line[start:end])))
    return part_numbers


def get_gear_number(gear_i, line, above_line, below_line):
    left_index = gear_i - 1 if gear_i > 0 else 0
    right_index = gear_i + 1 if gear_i < len(line) else len(line) - 1

    numbers = []
    for l in [line, above_line, below_line]:
        line_hits = find_pattern_indexes(NUMERIC, "".join(l))
        for hit in line_hits:
            if (hit[0] <= right_index and hit[0] >= left_index) or (
                hit[1] - 1 <= right_index and hit[1] - 1 >= left_index
            ):
                number = l[hit[0] : hit[1]]
                numbers.append(int("".join(number)))
    if not len(numbers) == 2:
        return 0
    else:
        return numbers[0] * numbers[1]


def find_gear_numbers(transformed, numbers, all_gears):
    gear_numbers = []

    for i, line in enumerate(transformed):
        line_gears = all_gears[i]
        if not line_gears:
            continue

        # Get above + below rows
        if i == 0:
            above_line = None
        else:
            above_line = transformed[i - 1]
        if i == len(numbers) - 1:
            below_line = None
        else:
            below_line = transformed[i + 1]

        for gear in line_gears:
            gear_i = gear[0]
            gear_numbers.append(get_gear_number(gear_i, line, above_line, below_line))
    return gear_numbers


def main_1(input):
    transformed_input, number_i, _ = transform_input(input)
    part_numbers = find_part_numbers(transformed_input, number_i)
    answer = sum(part_numbers)
    print(f"PT 1 ANSWER: {answer}")


def main_2(input):
    transformed_input, number_i, gear_i = transform_input(input, GEARS)
    gear_numbers = find_gear_numbers(transformed_input, number_i, gear_i)
    answer = sum(gear_numbers)
    print(f"PT 2 ANSWER: {answer}")


if __name__ == "__main__":
    with open("2023/day_3/input.txt", "r") as f:
        input = f.readlines()
    # main_1(input)
    main_2(input)
