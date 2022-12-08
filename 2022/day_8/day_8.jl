function main(in_file)
    trees = []
    open(in_file) do f
        trees = readlines(f)
    end
    n_visible_trees = 0
    for (x, _) in enumerate(trees)
        for (y, _) in enumerate(trees[x])
            n_visible_trees += is_tree_visible(trees, x, y)
        end
    end
    println("Number of visible trees: ", n_visible_trees)

    highest_scenic_score = 0
    for (x, _) in enumerate(trees)
        for (y, _) in enumerate(trees[x])
            tree_score = scenic_score(trees, x, y)
            if tree_score > highest_scenic_score
                highest_scenic_score = tree_score
            end
        end
    end
    println("Highest possible scenic score: ", highest_scenic_score)
end


function scenic_score(trees, x_pos, y_pos)
    row = [parse(Int, i) for i in trees[x_pos]]
    col = [parse(Int, i[y_pos]) for i in trees]
    return score_from_vector(row, y_pos) * score_from_vector(col, x_pos)
end

function score_from_vector(tree_line, pos)
    tree_height = tree_line[pos]
    left_view = reverse(tree_line[1:pos-1])
    right_view = tree_line[pos+1:length(tree_line)]
    left = view_score(left_view, tree_height)
    right = view_score(right_view, tree_height)
    return left * right
end

function view_score(view, tree_height)
    score = 0
    for this_height in view
        score += 1
        if this_height >= tree_height
            break
        end
    end
    return score
end


function is_tree_visible(trees, x_pos, y_pos)
    row = [parse(Int, i) for i in trees[x_pos]]
    col = [parse(Int, i[y_pos]) for i in trees]
    return visible_from_vector(row, y_pos) || visible_from_vector(col, x_pos)
end


function visible_from_vector(tree_line, pos)
    tree_height = tree_line[pos]
    # from the left
    visible_left = true
    for i in 1:pos-1
        if tree_line[i] >= tree_height
            visible_left = false
        end
    end
    # from the right
    visible_right = true
    for i in pos+1:length(tree_line)
        if tree_line[i] >= tree_height
            visible_right = false
        end
    end
    return visible_left || visible_right
end


main("input.txt")