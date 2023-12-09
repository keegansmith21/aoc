from math import lcm


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


def find_cycle_length(node, nodes, instructions):
    step = 0
    z_instructions = []
    z_instruction_steps = []
    while True:
        instruction = instructions[step % len(instructions)]
        node = nodes[node][instruction]
        if node[-1] == "Z":
            instruction_n = step % len(instructions)
            if instruction_n in z_instructions:
                break
            z_instructions.append(instruction_n)
            z_instruction_steps.append(step)
        step += 1
    return step - z_instruction_steps[-1]


def main_2(input):
    nodes, instructions = fmt(input)

    step_nodes = [n for n in list(nodes.keys()) if n[-1] == "A"]
    cycle_steps = []
    for node in step_nodes:
        cycle_steps.append(find_cycle_length(node, nodes, instructions))
    answer = lcm(*cycle_steps)

    print(f"PT 2 ANSWER: {answer}")
    pass


if __name__ == "__main__":
    with open("2023/day_8/input.txt", "r") as f:
        input = f.readlines()
    # main_1(input)
    main_2(input)
