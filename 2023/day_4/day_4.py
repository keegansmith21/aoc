def card_value(winning, mine):
    value = 0
    for n in mine:
        if n in winning:
            value *= 2
            if value == 0:
                value += 1
    return value


def matching_values(winning, mine):
    values = 0
    for n in mine:
        if n in winning:
            values += 1
    return values


def read_line(line):
    winning = line.strip().split(":")[-1].split("|")[0].strip().split(" ")
    winning = [int(i) for i in winning if i]
    mine = line.strip().split(":")[-1].split("|")[1].strip().split(" ")
    mine = [int(i) for i in mine if i]
    return winning, mine


def main_1(input):
    values = []
    for line in input:
        winning, mine = read_line(line)
        values.append(card_value(winning, mine))
    answer = sum(values)
    print(f"PT 1 ANSWER: {answer}")


def main_2(input):
    original_cards = []
    copies = {}
    for i, line in enumerate(input):
        original_cards.append(read_line(line))
        copies[i] = 1

    cards = original_cards.copy()
    for i, card in enumerate(cards):
        matching = matching_values(card[0], card[1])
        for _ in range(copies[i]):  # for each copy of this card
            for m in range(matching):
                key = i + m + 1
                if key in copies:
                    copies[key] += 1  # add a copy to the next card
    answer = sum(copies.values())
    print(f"PT 2 ANSWER: {answer}")


if __name__ == "__main__":
    with open("2023/day_4/input.txt", "r") as f:
        input = f.readlines()
    main_1(input)
    main_2(input)
