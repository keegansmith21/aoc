function main(in_file)

    inputs = []
    open(in_file) do f
        inputs = readlines(f)
    end
    x_cycle_cmds = parse_inputs(inputs)
    x_cycles = parse_x_cycles(x_cycle_cmds)
    signal_strength = [i * x for (i, x) in enumerate(x_cycles)]
    signal_sum = sum([signal_strength[i*40-20] for i in 1:6])
    println("Signal sum: $(signal_sum)")

    # Part 2
    sprite_locations = [[x - 1, x, x + 1] for x in x_cycles]
    crt = [i in sprite_locations[i] ? "#" : "." for i in 2:length(x_cycles)]
    line_indices = [[(i - 1) * 40 + 1, i * 40] for i in 1:6]
    render = [crt[s:e] for (s, e) in line_indices]
    for r in render
        println(join(r, ""))
    end
    #println(crt)
    #println(sprite_locations)
    println(x_cycles[7:11])
end


function parse_inputs(inputs)
    cycle_cmds = []
    for cmd in inputs
        push!(cycle_cmds, 0)
        if cmd != "noop"
            val = parse(Int, split(cmd, " ")[end])
            push!(cycle_cmds, val)
        end
    end
    return cycle_cmds

end


function parse_x_cycles(cycle_cmds)
    x_cycles = [1]
    for cmd in cycle_cmds
        push!(x_cycles, x_cycles[end] + cmd)
    end
    return x_cycles
end


main("test_input.txt") # should return 13140
#main("input.txt")