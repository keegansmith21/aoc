function main(in_file)
    double_ups = 0
    overlaps = 0
    open(in_file, "r") do f
        for line in readlines(f)
            elf_1, elf_2 = read_assignments(line)
            double_ups += isempty(setdiff(elf_1, elf_2)) || isempty(setdiff(elf_2, elf_1))
            overlaps += any_overlap(elf_1, elf_2)
        end
    end
    println("Number of assignment ranges with duplicated areas: ", double_ups)
    println("Number of assignment ranges with any overlapping areas: ", overlaps)
end



function read_assignments(line)
    fmt_line = split(line, ",")
    range_1 = split(fmt_line[1], "-")
    range_2 = split(fmt_line[2], "-")
    a1 = collect(parse(Int, range_1[1]):parse(Int, range_1[2]))
    a2 = collect(parse(Int, range_2[1]):parse(Int, range_2[2]))
    return a1, a2
end


function any_overlap(a, b)
    for i in a
        if i in b
            return true
        end
    end
    return false
end


main("input.txt")