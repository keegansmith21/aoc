MAP_FROM_ABOVE = {
    "|": {"|": (0, -1), "L": 1, "J": (-1, -1)},
    "7": {"|": (0, (-1, -1)), "L": 1, "J": (-1, -1)},
    "F": {"|": (0, (-1, -1)), "L": 1, "J": (-1, -1)},
}
MAP_FROM_BELOW = {
    "|": {"|": (0, 1), "F": 1, "7": (-1, 1)},
    "7": {"|": (0, 1), "F": 1, "7": (-1, 1)},
    "F": {"|": (0, 1), "F": 1, "7": (-1, 1)},
}
MAP_FROM_LEFT = {
    "-": {"-": (1, 0), "7": (1, -1)},
    "F": {"|": (1, 0), "J": (-1, -1)},
    "F": {"|": (1, 0), "F": (1, 0), "7": (1, 0)},
}
MOVE_UP = (-1, 0)
MOVE_DOWN = (1, 0)
MOVE_RIGHT = (0, 1)
MOVE_LEFT = (0, -1)

INSTRUCTIONS_UP = {"|": (MOVE_UP), "7": (MOVE_LEFT), "F": (MOVE_RIGHT)}
INSTRUCTIONS_DOWN = {"|": (MOVE_DOWN), "L": (MOVE_RIGHT), "J": (MOVE_LEFT)}
INSTRUCTIONS_LEFT = {"-": (MOVE_LEFT), "L": (MOVE_UP), "F": (MOVE_DOWN)}
INSTRUCTIONS_RIGHT = {"-": (MOVE_RIGHT), "J": (MOVE_UP), "7": (MOVE_DOWN)}


def fmt(input):
    fmtd = []
    for i, l in enumerate(input):
        fmtd.append(list(l.strip()))
        try:
            if l.index("S"):
                s_idx = (i, l.index("S"))
        except ValueError:
            pass

    return fmtd, s_idx


def instructions_from_cmd(cmd):
    if cmd == MOVE_UP:
        return INSTRUCTIONS_UP
    if cmd == MOVE_DOWN:
        return INSTRUCTIONS_DOWN
    if cmd == MOVE_LEFT:
        return INSTRUCTIONS_LEFT
    if cmd == MOVE_RIGHT:
        return INSTRUCTIONS_RIGHT


def execute_move(grid, s, cmd):
    new_idx = (s[0] + cmd[0], s[1] + cmd[1])
    new_pipe = grid[new_idx[0]][new_idx[1]]
    return new_pipe, new_idx


def traverse(grid, s_i):
    found = False
    loops = []
    for s_inst in (INSTRUCTIONS_UP, INSTRUCTIONS_DOWN, INSTRUCTIONS_LEFT, INSTRUCTIONS_RIGHT):
        if found == True:
            loops.append(loop)
            found = False
        steps = 0
        idx = s_i
        if s_inst == INSTRUCTIONS_UP or INSTRUCTIONS_DOWN:
            pipe = "|"
        else:
            pipe = "-"
        loop = [s_i]
        instructions = s_inst
        while True:
            move_cmd = instructions.get(pipe)
            if not move_cmd:
                break

            pipe, idx = execute_move(grid, idx, move_cmd)
            loop.append(idx)

            if not instructions_from_cmd(move_cmd).get(pipe):  # Move not allowed
                if pipe == "S":
                    found = True
                    loop = loop[::-1]
                break

            instructions = instructions_from_cmd(move_cmd)
            steps += 1

    return loops


def is_inside(element, grid, loop):
    north_elements = ["|", "J", "L"]
    row = element[0]
    check_range = (0, element[1])
    count = 0
    for i in range(*check_range):
        if (row, i) in loop:
            if grid[row][i] in north_elements:
                count += 1
    if bool(count % 2):
        return True
    else:
        return False


def get_elements_inside_loop(grid, loop):
    count = 0
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            if (y, x) in loop:
                continue
            if is_inside((y, x), grid, loop):
                count += 1
    return count


def main_1(input):
    grid, s_i = fmt(input)
    loops = traverse(grid, s_i)
    loop_len = (len(l) for l in loops)

    answer = max(loop_len) // 2
    print(f"PT 1 ANSWER: {answer}")


def main_2(input):
    grid, s_i = fmt(input)
    loops = traverse(grid, s_i)
    loop = max(loops, key=len)

    # Pretty picture
    grid_max_y = len(grid)
    grid_max_x = len(grid[0])
    loop_map = []
    for j in range(0, grid_max_y):
        row_map = []
        for i in range(0, grid_max_x):
            if (j, i) in loop:
                row_map.append(grid[j][i])
            else:
                row_map.append(".")
        loop_map.append(row_map)

    with open("2023/day_10/loop_map.txt", "w") as f:
        for i in loop_map:
            f.write("".join(i) + "\n")

    n_inside = get_elements_inside_loop(grid, loop)

    print(f"PT 2 ANSWER: {n_inside}")


if __name__ == "__main__":
    with open("2023/day_10/input.txt", "r") as f:
        input = f.readlines()
    main_1(input)
    main_2(input)
