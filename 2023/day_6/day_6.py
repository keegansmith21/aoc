from concurrent.futures import ProcessPoolExecutor


def fmt(input):
    times = input[0].split(":")[-1].strip().split(" ")
    dists = input[1].split(":")[-1].strip().split(" ")
    times = [t for t in times if t]
    dists = [d for d in dists if d]
    return [(int(t), int(d)) for t, d in zip(times, dists)]


def fmt2(input):
    times = input[0].split(":")[-1].strip().split(" ")
    dists = input[1].split(":")[-1].strip().split(" ")
    times = [t for t in times if t]
    dists = [d for d in dists if d]
    time = int("".join(times))
    dist = int("".join(dists))
    return time, dist


def d_travelled(t_held, t_total):
    return t_held * (t_total - t_held)


def race_dists(t_total):
    time_held = list(range(0, t_total))
    return [d_travelled(t_h, t_total) for t_h in time_held]


def range_wins(t_range, t_total, dist):
    wins = 0
    for t_held in t_range:
        if d_travelled(t_held, t_total) >= dist:
            wins += 1
    return wins


def main_1(input):
    races = fmt(input)
    n_wins = []
    for t_total, d_best in races:
        dists = race_dists(t_total)
        race_wins = [d for d in dists if d >= d_best]
        n_wins.append(len(race_wins))
    answer = 1
    for w in n_wins:
        answer *= w
    print(f"PT 1 ANSWER: {answer}")


def main_2(input):
    time, dist = fmt2(input)
    wins = range_wins(range(0, time), time, dist)
    print(f"PT 2 ANSWER: {wins}")


if __name__ == "__main__":
    #    with open("2023/day_5/test_input.txt", "r") as f:
    with open("2023/day_6/input.txt", "r") as f:
        input = f.readlines()
    # main_1(input)
    main_2(input)
