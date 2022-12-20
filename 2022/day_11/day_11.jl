OPERAND_MAP = Dict("+" => +, "-" => -, "/" => /, "*" => *, "^" => ^)

function main(in_file)
    monkeys = parse_input(in_file)
    round_inspections = simulate_rounds(monkeys, 20, 3)
    println("Part 1 results:")
    monkeys = parse_input(in_file)
    calc_results(round_inspections, monkeys)
    round_inspections = simulate_rounds(monkeys, 10000, 1)
    println("Part 2 results:")
    calc_results(round_inspections, monkeys)

end


function parse_input(in_file)
    monkeys = Dict{Int,Dict}()
    lines = []
    open(in_file) do f
        lines = readlines(f)
    end
    monkey_no = nothing
    for line in lines
        if occursin("Monkey", line)
            monkey_no = parse(Int, split(line, ":")[1][end])
            monkeys[monkey_no] = Dict{String,Any}()
        elseif occursin("Starting items:", line)
            monkeys[monkey_no]["items"] = [parse(Int, i) for i in split(split(line, "Starting items:")[end], ",")]
        elseif occursin("Operation:", line)
            operation = split(line, "new = old ")[end]
            operand = split(operation, " ")[1]
            val = split(operation, " ")[end]
            if operand == "*" && val == "old" # Handle squaring
                operand = "^"
                val = 2
            else
                val = parse(Int, val)
            end
            monkeys[monkey_no]["operation"] = Dict()
            monkeys[monkey_no]["operation"]["operand"] = OPERAND_MAP[operand]
            monkeys[monkey_no]["operation"]["value"] = val
        elseif occursin("Test:", line)
            monkeys[monkey_no]["test"] = Dict()
            monkeys[monkey_no]["test"]["condition"] = parse(Int, split(line, " ")[end])
        elseif occursin("true: throw to monkey", line)
            monkeys[monkey_no]["test"]["true"] = parse(Int, split(line, " ")[end])
        elseif occursin("false: throw to monkey", line)
            monkeys[monkey_no]["test"]["false"] = parse(Int, split(line, " ")[end])
        end
    end
    return monkeys
end


function simulate_rounds(monkeys, n_rounds, worry_divisor)
    round_inspections = Vector{Int}[]
    for r in 1:n_rounds
        monkeys, inspections = simulate_round(monkeys, worry_divisor)
        push!(round_inspections, inspections)
    end
    return round_inspections
end


function simulate_round(monkeys, worry_divisor)
    inspections = fill(Int(0), length(keys(monkeys)))
    supermod = prod([monkeys[i]["test"]["condition"] for i in keys(monkeys)])
    for monkey_no in sort(collect(keys(monkeys)))
        for _ in eachindex(monkeys[monkey_no]["items"])
            # Monkey inspects the next item on the list
            monkeys[monkey_no]["items"][1] = monkeys[monkey_no]["operation"]["operand"](monkeys[monkey_no]["items"][1], monkeys[monkey_no]["operation"]["value"])
            inspections[monkey_no+1] += 1

            # Item isn't damaged, divide worry by divisor
            monkeys[monkey_no]["items"][1] = mod(monkeys[monkey_no]["items"][1], supermod) # Part 2 adjustment
            monkeys[monkey_no]["items"][1] ÷= worry_divisor

            # Monkey tests you to see where to throw the item
            if mod(monkeys[monkey_no]["items"][1], monkeys[monkey_no]["test"]["condition"]) == 0
                # Throw to monkey in 'true' condition
                recipient = monkeys[monkey_no]["test"]["true"]
            else
                recipient = monkeys[monkey_no]["test"]["false"]
            end

            # Throw the item
            push!(monkeys[recipient]["items"], popfirst!(monkeys[monkey_no]["items"]))

        end
    end
    return monkeys, inspections
end


function calc_results(round_inspections, monkeys)
    println("Final Items:")
    for m in eachindex(collect(keys(monkeys)))
        println(monkeys[m-1]["items"])
    end
    summed_inspections = []
    for i in eachindex(collect(keys(monkeys)))
        push!(summed_inspections, sum([round[i] for round in round_inspections]))
    end
    for i in eachindex(summed_inspections)
        println("Monkey $(i-1) inspected items $(summed_inspections[i]) times")
    end
    println("The level of monkey business is $(sort(summed_inspections)[end] * sort(summed_inspections)[end-1])")
end

main("test_input.txt") # Answer should be 10605/2713310158
main("input.txt")