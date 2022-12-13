
CMD_MAPPING = Dict("U" => [0, 1], "D" => [0, -1], "R" => [1, 0], "L" => [-1, 0])

function main(in_file)
    commands = read_commands(in_file)
    # tail_positions = parse_commands(commands, 2)
    # n_tail_positions = length(unique(tail_positions))
    # println("Unique tail positions for two knot: $(n_tail_positions)")

    tail_positions = parse_commands(commands, 10)
    n_tail_positions = length(unique(tail_positions))
    println("Unique tail positions for ten knots: $(n_tail_positions)")
end


function read_commands(file)
    input = []
    open(file) do f
        input = readlines(f)
    end
    directions = [split(i, " ")[1] for i in input]
    n_steps = [parse(Int, split(i, " ")[end]) for i in input]
    commands = []
    for (d, n) in zip(directions, n_steps)
        append!(commands, repeat([d], n))
    end
    return commands
end


function parse_commands(commands, n_knots)
    tail_tracking = []
    knot_positions = [[0, 0] for _ in 1:n_knots]
    for cmd in commands
        knot_positions[1] += CMD_MAPPING[cmd]
        for k in 2:n_knots
            knot_positions[k] += tail_move(knot_positions[k-1], knot_positions[k])
        end
        append!(tail_tracking, knot_positions[2:n_knots])
        #println(knot_positions)
    end
    return tail_tracking
end


function tail_move(head, tail)
    tail_move = [0, 0]
    diff = [head[1] - tail[1], head[2] - tail[2]]
    if abs(diff[1]) == 2
        tail_move[1] = 1
        if abs(diff[2]) >= 1
            tail_move[2] = 1
        end
    elseif abs(diff[2]) == 2
        tail_move[2] = 1
        if abs(diff[1]) >= 1
            tail_move[1] = 1
        end
    end
    # Now fix for negative movement directions
    diff_sign = [(diff[1] < 1) ? -1 : 1, (diff[2] < 1) ? -1 : 1]
    tail_move = tail_move .* diff_sign
    return tail_move
end


main("input.txt")