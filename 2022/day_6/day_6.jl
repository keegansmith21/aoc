function main(in_file)
    open(in_file, "r") do f
        cursor = find_marker(readline(f), 4)
        println("Part 1 Marker occurs after character ", cursor)
    end
    open(in_file, "r") do f
        cursor = find_marker(readline(f), 14)
        println("Part 2 Marker occurs after character ", cursor)
    end
end


function find_marker(input, marker_size)
    cursor = marker_size
    while cursor != length(input)
        if is_marker(input[cursor-marker_size+1:cursor], marker_size)
            return cursor
        end
        cursor += 1
    end
end

function is_marker(input, marker_size)
    @assert(length(input) == marker_size)
    return length(Set(input)) == marker_size
end


main("input.txt")