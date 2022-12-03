function main(in_file)

    priority = 0
    open(in_file, "r") do f
        for rucksack_items in readlines(f)
            letter = find_common_letter(rucksack_items)
            priority += letter_priority(letter)
        end
    end
    print("Total priority: ")
    println(priority)
end


function find_common_letter(rucksack_items)
    first_half, second_half = get_compartments(rucksack_items)
    for l in first_half
        if occursin(l, second_half)
            return l
        end
    end
end


function get_compartments(rucksack_items)
    total_items = Int32(length(rucksack_items))
    n_compartment_items = Int32(total_items / 2)
    first_half = rucksack_items[1:n_compartment_items]
    second_half = rucksack_items[n_compartment_items+1:total_items]
    return first_half, second_half
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