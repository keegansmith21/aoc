def fmt(input):
    return input[0].strip().split(",")


def hash_string(s):
    cv = 0
    for char in list(s):
        cv += ord(char)
        cv *= 17
        cv %= 256
    return cv


def label_in_box(box, label):
    for i, v in enumerate(box):
        if v.split(" ")[0] == label:
            return i

    return False


def box_power(box, box_n):
    power = 0
    for i, v in enumerate(box):
        f = v.split(" ")[1]
        power += box_n * (i + 1) * int(f)
    return power


def main_1(input):
    steps = fmt(input)
    answer = 0
    for step in steps:
        answer += hash_string(step)

    print(f"PT 1 ANSWER: {answer}")


def main_2(input):
    steps = fmt(input)
    boxes = {i: [] for i in range(256)}
    for step in steps:
        if step.endswith("-"):
            label = step[:-1]
            box_no = hash_string(label)
            i = label_in_box(boxes[box_no], label)
            if i is False:
                continue
            else:
                del boxes[box_no][i]

        else:
            label = step.split("=")[0]
            f = step.split("=")[-1]
            box_no = hash_string(label)
            i = label_in_box(boxes[box_no], label)
            if i is False:
                boxes[box_no].append(f"{label} {f}")
            else:
                boxes[box_no][i] = f"{label} {f}"

    answer = sum([box_power(b, i + 1) for i, b in boxes.items()])
    print(f"PT 2 ANSWER: {answer}")


if __name__ == "__main__":
    with open("2023/day_15/input.txt", "r") as f:
        input = f.readlines()
    main_1(input)
    main_2(input)
