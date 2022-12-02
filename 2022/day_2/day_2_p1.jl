function main(in_file)
    total_points = 0
    open(in_file, "r") do f
        for l in readlines(f)
            opt, my = split(l)
            total_points += calculate_points(opt, my)
        end
    end
    print("Total Points: ")
    println(total_points)
end


function calculate_points(opt_in, my_in)
    opt_in = standardise_input(opt_in)
    my_in = standardise_input(my_in)
    points = points_from_choice(my_in) + win_draw_loss(opt_in, my_in)
    return points
end


function standardise_input(input)
    if input == "A" || input == "X"
        return "Rock"
    elseif input == "B" || input == "Y"
        return "Paper"
    elseif input == "C" || input == "Z"
        return "Scizzors"
    end
end


function win_draw_loss(opt_in, my_in)
    points = 0
    if opt_in == my_in
        points = 3
    elseif opt_in == "Rock"
        if my_in == "Paper"
            points = 6
        end
    elseif opt_in == "Paper"
        if my_in == "Scizzors"
            points = 6
        end
    else # opt_in = Scizzors
        if my_in == "Rock"
            points = 6
        end
    end
    return points
end

function points_from_choice(choice)
    points = 1
    if choice == "Paper"
        points = 2
    elseif choice == "Scizzors"
        points = 3
    end
    return points
end


main("input.txt")