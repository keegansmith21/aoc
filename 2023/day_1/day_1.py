import re

number_words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def replace_words(line):
    newline = list(line)
    for i in range(len(line)):
        for k, v in number_words.items():
            if line[i:].startswith(k):
                newline[i] = v
    newline = "".join(newline)
    return newline


def get_calibration_value(line):
    digits = re.compile(r"\d").findall(line)
    val = int(digits[0] + digits[-1])
    return val


def main_1(input):
    calibration_values = [get_calibration_value(i) for i in input]
    calibration_value = sum(calibration_values)
    print(f"PT 1 CALIBRATION_VALUE: {calibration_value}")


def main_2(input):
    new_inputs = [replace_words(i) for i in input]
    calibration_values = [get_calibration_value(i) for i in new_inputs]
    calibration_value = sum(calibration_values)
    print(f"PT 2 CALIBRATION_VALUE: {calibration_value}")


if __name__ == "__main__":
    with open("2023/day_1/input.txt", "r") as f:
        input = f.readlines()
    main_1(input)
    main_2(input)
