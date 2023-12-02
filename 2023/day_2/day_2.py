POSSIBLE = {"red": 12, "green": 13, "blue": 14}


def is_possible(draw):
    all_cubes = draw.split(",")
    for cube_set in all_cubes:
        value, colour = cube_set.split()
        if int(value) > POSSIBLE[colour]:
            return False
    return True


def game_value(line):
    game_id, draws = get_games(line)
    for draw in draws:
        if not is_possible(draw):
            game_id = 0
            break
    return game_id


def get_games(line):
    line = line.strip().split(":")
    game_id = int(line[0].split("Game")[-1])
    games = line[-1].split(";")
    return game_id, games


def game_power(line):
    highest_values = {"red": 0, "green": 0, "blue": 0}
    _, games = get_games(line)
    for draw in games:
        all_cubes = draw.split(",")
        for cube_set in all_cubes:
            value, colour = cube_set.split()
            if int(value) > highest_values[colour]:
                highest_values[colour] = int(value)
    power = 1
    for v in highest_values.values():
        power *= v
    return power


def main_1(input):
    answer = sum([game_value(i) for i in input])
    print(f"PT 1 ANSWER: {answer}")


def main_2(input):
    answer = sum([game_power(i) for i in input])
    print(f"PT 2 ANSWER: {answer}")


if __name__ == "__main__":
    with open("2023/day_2/input.txt", "r") as f:
        input = f.readlines()
    main_1(input)
    main_2(input)
