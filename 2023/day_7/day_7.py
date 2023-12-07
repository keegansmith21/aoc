def fmt(input):
    hands = []
    bids = []
    for line in input:
        hands.append(line.strip().split(" ")[0])
        bids.append(int(line.strip().split(" ")[-1]))
    return hands, bids


def hand_type(hand):
    possibilities = {
        "A": 0,
        "K": 0,
        "Q": 0,
        "J": 0,
        "T": 0,
        "9": 0,
        "8": 0,
        "7": 0,
        "6": 0,
        "5": 0,
        "4": 0,
        "3": 0,
        "2": 0,
    }
    for card in hand:
        possibilities[card[0]] += 1

    counts = sorted(list(possibilities.values()), reverse=True)

    if counts[0] == 5:
        return "7"
    elif counts[0] == 4:
        return "6"
    elif counts[0] == 3 and counts[1] == 2:
        return "5"
    elif counts[0] == 3:
        return "4"
    elif counts[0] == 2 and counts[1] == 2:
        return "3"
    elif counts[0] == 2:
        return "2"
    else:
        return "1"


def split_hands(hands, bids):
    # Split all hands into six lists.
    split_hands = {"1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": []}
    for hand, bid in zip(hands, bids):
        type = hand_type(hand)
        split_hands[type].append((hand, bid))
    return split_hands


def hand_type_2(hand):
    possibilities = {
        "A": 0,
        "K": 0,
        "Q": 0,
        "J": 0,
        "T": 0,
        "9": 0,
        "8": 0,
        "7": 0,
        "6": 0,
        "5": 0,
        "4": 0,
        "3": 0,
        "2": 0,
    }
    for card in hand:
        possibilities[card[0]] += 1

    pos_no_j = {i: possibilities[i] for i in possibilities if i != "J"}
    counts_no_j = sorted(list(pos_no_j.values()), reverse=True)
    counts_no_j[0] += possibilities["J"]

    if counts_no_j[0] == 5:
        return "7"
    elif counts_no_j[0] == 4:
        return "6"
    elif counts_no_j[0] == 3 and counts_no_j[1] == 2:
        return "5"
    elif counts_no_j[0] == 3:
        return "4"
    elif counts_no_j[0] == 2 and counts_no_j[1] == 2:
        return "3"
    elif counts_no_j[0] == 2:
        return "2"
    else:
        return "1"


def split_hands_2(hands, bids):
    # Split all hands into six lists.
    split_hands = {"1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": []}
    for hand, bid in zip(hands, bids):
        type = hand_type_2(hand)
        split_hands[type].append((hand, bid))
    return split_hands


def order_hands_on_highest(
    hands_bids,
    strength_map={
        "A": 13,
        "K": 12,
        "Q": 11,
        "J": 10,
        "T": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1,
    },
):
    hands = [hb[0] for hb in hands_bids]
    hand_strengths = []
    for hand in hands:
        n = 7
        strength = 0
        for v in list(hand):
            strength += strength_map[v] * (14 ** (n))
            n -= 1
        hand_strengths.append(strength)
    # sort each hand based on its strength
    sorted_hands = [x for _, x in sorted(zip(hand_strengths, hands_bids), reverse=True)]
    return sorted_hands


def main_1(input):
    hands, bids = fmt(input)
    hands_typed = split_hands(hands, bids)
    winnings = 0
    ranks = []
    for type_group in sorted(list(hands_typed.keys()), reverse=True):
        ranks.extend(order_hands_on_highest(hands_typed[type_group]))
    for i, ranked_input in enumerate(ranks):
        winnings += ranked_input[1] * (len(ranks) - i)

    print(f"PT 1 ANSWER: {winnings}")
    pass


def main_2(input):
    hands, bids = fmt(input)
    hands_typed = split_hands_2(hands, bids)
    winnings = 0
    ranks = []
    for type_group in sorted(list(hands_typed.keys()), reverse=True):
        ranks.extend(
            order_hands_on_highest(
                hands_typed[type_group],
                strength_map={
                    "A": 13,
                    "K": 12,
                    "Q": 11,
                    "T": 10,
                    "9": 9,
                    "8": 8,
                    "7": 7,
                    "6": 6,
                    "5": 5,
                    "4": 4,
                    "3": 3,
                    "2": 2,
                    "J": 1,
                },
            )
        )
    for i, ranked_input in enumerate(ranks):
        winnings += ranked_input[1] * (len(ranks) - i)

    print(f"PT 2 ANSWER: {winnings}")
    pass


if __name__ == "__main__":
    with open("2023/day_7/input.txt", "r") as f:
        input = f.readlines()
    main_1(input)
    main_2(input)
