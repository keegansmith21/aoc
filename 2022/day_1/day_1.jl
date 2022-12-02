function main(in_file)
    elves_calories = []
    this_elf_calories = 0
    open(in_file, "r") do f
        for l in readlines(f)
            # Count the calories for each elf
            if !isempty(l)
                this_elf_calories += parse(Int32, l)
            else # We have counted each snack for this elf
                push!(elves_calories, this_elf_calories)
                this_elf_calories = 0
            end
        end
    end
    elves_calories = sort(elves_calories, rev=true)
    print("Top 3 elf calories: ")
    println(elves_calories[1:3])
    print("Combined: ")
    println(sum(elves_calories[1:3]))
end

main("input.txt")