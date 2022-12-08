using FilePaths

function main(in_file)
    open(in_file, "r") do f
        directories = disk_usage(readlines(f))
        total = sum_of_dirs(directories)
        println("Sum of file usage where files <= 100000: ", total)
        free_space = 7e7 - directories["/"]
        println("Current free space: ", free_space)
        rem_dir_space = 3e7 - free_space
        println("Find directory with size of at least ", rem_dir_space)
        size, name = closest_dir_over(directories, rem_dir_space)
        println("Delete the directory:", name, " which will free up ", size, " bytes")
    end
end


function disk_usage(lines)
    directories = Dict{String,Int}()
    cwd = ""
    for l in lines
        parts = split(l)
        if parts[1] == "\$" && parts[2] == "cd"
            if parts[3] == ".."
                cwd = dirname(cwd)
                println(cwd)
            else
                cwd = joinpath(cwd, parts[3])
                directories[cwd] = 0
                println(cwd)
            end
        elseif tryparse(Int, parts[1]) !== nothing
            usage = parse(Int, split(l, " ")[1])
            add_size_to_dirs(cwd, directories, usage)
        end
    end
    return directories
end


function add_size_to_dirs(cwd, dirs, size)
    wds = split(cwd, "/")
    for i in 1:length(wds)
        d = wds[1:length(wds)-i+1]
        d = join(d, "/")
        if d == ""
            d = "/"
        end
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
    chosen_size = 1e10
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