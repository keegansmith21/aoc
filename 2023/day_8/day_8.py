from concurrent.futures import ProcessPoolExecutor, as_completed


def most_common_item(lst):
    count_dict = {}

    for item in lst:
        count_dict[item] = count_dict.get(item, 0) + 1

    common_item = max(count_dict, key=count_dict.get)
    count = count_dict[common_item]

    return common_item, count


def fmt(input):
    instructions = input[0].strip()
    nodes = {}
    for line in input[2:]:
        line_stuff = line.strip().split("=")
        name = line_stuff[0].strip()
        left = line_stuff[1].strip()[1:4]
        right = line_stuff[1].strip()[6:9]
        nodes[name] = {"L": left, "R": right}

    return nodes, instructions


def main_1(input):
    nodes, instructions = fmt(input)
    steps = 0
    node = "AAA"
    while True:
        print(steps)
        if node == "ZZZ":
            break
        instruction = instructions[steps % len(instructions)]
        steps += 1
        node = nodes[node][instruction]

    print(f"PT 1 ANSWER: {steps}")


def get_zs(node, nodes, instructions, step_s, step_e):
    zs = []
    for i in range(step_s, step_e):
        instruction = instructions[i % len(instructions)]
        node = nodes[node][instruction]
        if node[-1] == "Z":
            zs.append(i)

    return zs, node


def main_2_2(input):
    nodes, instructions = fmt(input)
    step_nodes = [n for n in list(nodes.keys()) if n[-1] == "A"]

    i = int(1e7)
    j = 0
    c = 0
    while True:
        with ProcessPoolExecutor(max_workers=len(step_nodes)) as executor:
            futures = []
            for n in step_nodes:
                futures.append(executor.submit(get_zs, n, nodes, instructions, j, j + i))

            all_zs = []
            step_nodes = []
            for future in as_completed(futures):
                zs, node = future.result()
                all_zs.extend(zs)
                step_nodes.append(node)

            item, count = most_common_item(all_zs)
            print(count, item)
            if count == len(step_nodes):
                break
            j += i

    print(f"PT 2 ANSWER: {item}")


def main_2(input):
    nodes, instructions = fmt(input)

    step_nodes = [n for n in list(nodes.keys()) if n[-1] == "A"]
    n_nodes = len(step_nodes)
    steps = 0
    while True:
        ends_in = [n[-1] for n in step_nodes]
        n_zs = ends_in.count("Z")
        if n_zs > 2:
            print("".join(ends_in), n_zs)
        if n_zs == n_nodes:
            break

        instruction = instructions[steps % len(instructions)]
        steps += 1
        step_nodes = [nodes[n][instruction] for n in step_nodes]

    print(f"PT 2 ANSWER: {steps}")
    pass


if __name__ == "__main__":
    with open("2023/day_8/input.txt", "r") as f:
        input = f.readlines()
    # main_1(input)
    main_2_2(input)
