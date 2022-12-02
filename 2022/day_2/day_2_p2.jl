function main(in_file)
    total_points = 0
    open(in_file, "r") do f
        for l in readlines(f)
            opt, result = split(l)
            opt = standardise_input(opt)
            my, outcome_points = determine_choice(opt, result)
            total_points += outcome_points
            total_points += points_from_choice(my)
        end
    end
    print("Total Points: ")
    println(total_points)
end


function determine_choice(opt_in, result)
    # X = lose
    # Y = draw
    # Z = Win
    desired_outcome = 0
    if result == "Y"
        desired_outcome = 3
    elseif result == "Z"
        desired_outcome = 6
    end
    println(string("desired_outcome: ", desired_outcome))
    for choice in ["Rock", "Paper", "Scissors"]
        if win_draw_loss(opt_in, choice) == desired_outcome
            println(string(opt_in, " :: ", choice))
            return choice, desired_outcome
        end
    end
end


function standardise_input(input)
    if input == "A"
        return "Rock"
    elseif input == "B"
        return "Paper"
    else
        return "Scissors"
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
        if my_in == "Scissors"
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
    elseif choice == "Scissors"
        points = 3
    end
    return points
end


main("input.txt")