using FilePaths

function main(in_file)
    open(in_file, "r") do f
        directories = disk_usage(readlines(f))
        total_under = sum_of_dirs(directories)
        println("Sum of file usage where files <= 100000: ", total_under)
        total_usage = directories["/"]
        free_space = 7 * 10^7 - total_usage
        rem_dir_space = 3 * 10^7 - free_space
        size, name = closest_dir_over(directories, rem_dir_space)
        println("Delete the directory:", name, " which will free up ", size, " bytes")
    end
end


function disk_usage(lines)
    directories = Dict{String,Int}()
    cwd = ""
    total_usage = 0
    for l in lines
        parts = split(l)
        if parts[1] == "\$" && parts[2] == "cd"
            if parts[3] == ".."
                cwd = dirname(cwd)
            else
                cwd = joinpath(cwd, parts[3])
                directories[cwd] = 0
            end
        elseif tryparse(Int, parts[1]) !== nothing
            usage = parse(Int, parts[1])
            total_usage += usage
            add_size_to_dirs(cwd, directories, usage)
        end
    end
    return directories
end


function add_size_to_dirs(cwd, dirs, size)
    wds = splitpath(cwd)
    for i in 1:length(wds)
        d = wds[1:length(wds)-i+1]
        d = joinpath(d)
        dirs[d] += size
    end
end


function sum_of_dirs(dirs)
    total = 0
    for v in values(dirs)
        if v <= 100000
            total += v
        end
    end
    return total
end


function closest_dir_over(dirs, minimum)
    chosen_size = 1 * 10^10
    chosen_name = ""
    for (name, size) in dirs
        if size > minimum && size < chosen_size
            chosen_size = size
            chosen_name = name
        end
    end
    return chosen_size, chosen_name
end


main("input.txt")