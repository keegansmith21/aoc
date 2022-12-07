function main(in_file)
    starting_stack, orders = parse_file(in_file)
    ending_stack = execute_orders_pt1(starting_stack, orders)
    println("Final letters of each stack (part 1):")
    for stack in ending_stack
        println(last(stack), " ")
    end
    starting_stack, orders = parse_file(in_file)
    ending_stack = execute_orders_pt2(starting_stack, orders)
    println("Final letters of each stack (part 2):")
    for stack in ending_stack
        println(last(stack), " ")
    end
end


function execute_orders_pt1(stack, orders)
    for order in orders
        move_no, from_stack, to_stack = order
        for _ in 1:move_no
            push!(stack[to_stack], pop!(stack[from_stack]))
        end
    end
    return stack
end


function execute_orders_pt2(stack, orders)
    for order in orders
        move_no, from_stack_no, to_stack_no = order
        from_stack = stack[from_stack_no]
        move_barrier = length(from_stack) - move_no'
        append!(stack[to_stack_no], from_stack[move_barrier+1:end])
        stack[from_stack_no] = from_stack[1:move_barrier]
    end
    return stack
end


function parse_file(file)
    open(file, "r") do f
        input = readlines(f)

        # Find out where the linebreak is
        linebreak = 0
        for l in input
            linebreak += 1
            if isempty(l)
                break
            end
        end
        orders = get_orders(input[linebreak+1:length(input)])
        starting_arrangement = get_arrangement(input[1:linebreak-2])
        return starting_arrangement, orders
    end
end


function get_arrangement(lines)
    n_elements = Int((length(lines[1]) + 1) / 4)
    arrangement = [] # Create the skeleton arrangement
    for _ in 1:n_elements
        push!(arrangement, [])
    end
    for l in reverse(lines)
        for i in 1:n_elements
            letter_location = i * 4 - 2
            letter = l[letter_location]
            if letter != ' '
                push!(arrangement[i], letter)
            end
        end
    end
    return arrangement
end

function get_orders(lines)
    orders = []
    for l in lines
        l = split(l, " ")
        push!(orders, [parse(Int, l[2]), parse(Int, l[4]), parse(Int, l[6])])
    end
    return orders
end



main("input.txt")