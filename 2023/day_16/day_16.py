from copy import deepcopy


def fmt(input):
    return [list(i.strip()) for i in input]


def ray_trace(grid, start, dir, visited, calls, first=False):
    while True:
        if hash((start, dir)) in calls:
            return visited
        else:
            calls.append(hash((start, dir)))

        # Update the visited spaces
        if not first:
            visited[start[0]][start[1]] = "#"
        first = False

        # outside grid check
        next_pos = (start[0] + dir[0], start[1] + dir[1])
        if -1 in next_pos or len(grid) in next_pos or len(grid[0]) in next_pos:
            return visited

        next_space = grid[next_pos[0]][next_pos[1]]
        if next_space == ".":  # Continue
            start = next_pos
            continue

        elif next_space == "-":  # Horizontal splitter
            if dir[1] != 0:
                start = next_pos
                continue
            else:
                # Go left and right
                visited = ray_trace(grid, next_pos, (0, 1), visited, calls)
                visited = ray_trace(grid, next_pos, (0, -1), visited, calls)
                return visited

        elif next_space == "|":  # Vertical splitter
            if dir[0] != 0:
                start = next_pos
                continue
            else:
                # Go up and down
                visited = ray_trace(grid, next_pos, (1, 0), visited, calls)
                visited = ray_trace(grid, next_pos, (-1, 0), visited, calls)
                return visited

        elif next_space == "\\":
            dir = (dir[1], dir[0])
            start = next_pos
            continue
        elif next_space == "/":
            dir = (-dir[1], -dir[0])
            start = next_pos
            continue


def main_1(input):
    grid = fmt(input)
    visited = deepcopy(grid)
    visited = ray_trace(grid, (0, -1), (0, 1), visited, [], first=True)
    answer = sum([i.count("#") for i in visited])

    print(f"PT 1 ANSWER: {answer}")


def main_2(input):
    grid = fmt(input)

    answers = []
    # Top row
    print("Top row")
    for i in range(len(grid[0])):
        visited = deepcopy(grid)
        visited = ray_trace(grid, (-1, i), (1, 0), visited, [], first=True)
        answers.append(sum([i.count("#") for i in visited]))

    # Bottom row
    print("Bottom row")
    for i in range(len(grid[0])):
        visited = deepcopy(grid)
        visited = ray_trace(grid, (len(grid), i), (-1, 0), visited, [], first=True)
        answers.append(sum([i.count("#") for i in visited]))

    # Left column
    print("Left column")
    for i in range(len(grid)):
        visited = deepcopy(grid)
        visited = ray_trace(grid, (i, -1), (0, 1), visited, [], first=True)
        answers.append(sum([i.count("#") for i in visited]))

    # Right column
    print("Right column")
    for i in range(len(grid)):
        visited = deepcopy(grid)
        visited = ray_trace(grid, (i, len(grid[0])), (0, -1), visited, [], first=True)
        answers.append(sum([i.count("#") for i in visited]))

    print(f"PT 2 ANSWER: {max(answers)}")


if __name__ == "__main__":
    with open("2023/day_16/input.txt", "r") as f:
        input = f.readlines()
    main_1(input)
    main_2(input)
