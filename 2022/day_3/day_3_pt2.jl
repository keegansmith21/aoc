function main(in_file)

    priority = 0
    open(in_file, "r") do f
        counter = 1
        group_items = []
        for rucksack_items in readlines(f)
            push!(group_items, rucksack_items)
            if counter < 3
                counter += 1
                continue
            end
            letter = find_common_letter(group_items)
            priority += letter_priority(letter)
            # Reset the counter and items
            counter = 1
            group_items = []
        end
    end
    print("Total priority: ")
    println(priority)
end


function find_common_letter(group_items)
    first_rucksack = group_items[1]
    for l in first_rucksack
        if occursin(l, group_items[2]) && occursin(l, group_items[3])
            return l
        end
    end
end


function letter_priority(letter)
    if isuppercase(letter)
        priority = Int(letter) - 38 # A = 27, Z = 52
    else
        priority = Int(letter) - 96 # a = 1, z = 26
    end
    return priority
end


main("input.txt")