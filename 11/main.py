import math

f = open("./input.txt")
grid = [list(x.strip()) for x in f.readlines()]

empty_rows = [idx for idx, x in enumerate(grid) if "#" not in x]
empty_cols = [idx for idx, x in enumerate(zip(*grid)) if "#" not in x]

for col_idx, empty_col in enumerate(empty_cols):
    # Since we are mutating a list, we need to offset next value by the times we have mutated a list.
    for line in grid : 
        line.insert(empty_col + col_idx, ".")

for idx , empty_row in enumerate(empty_rows) :
    # Since we are mutating a list, we need to offset next value by the times we have mutated a list.
    grid.insert(empty_row + idx, grid[empty_row + idx])

coordinates = [(x,y) for y, row in enumerate(grid) for x, char in enumerate(row) if char == "#"]

def get_dist(start, target):
    x,y = start
    z,w = target
    return abs(x-z)+abs(y-w)

def get_paths(coordinates) :
    acc = []
    for idx, x in enumerate(coordinates):
        paths = [get_dist(x, end) for end in coordinates[idx:]]
        acc = acc + paths
    return acc

part_one = sum(get_paths(coordinates))

# print(part_one)


f_two = open("./input.txt")
part_two_grid = [list(x.strip()) for x in f_two.readlines()]

def get_offset_nums(axis, offsets) :
    nums = [x for x in axis]
    for idx, offset in enumerate(offsets) :
        for x_idx, item in enumerate(axis) :
            if item  > offset :
                nums[x_idx] = nums[x_idx] + 1000000 -1

    return nums

pt_coordinates = [(x,y) for y, row in enumerate(part_two_grid) for x, char in enumerate(row) if char == "#"]

pt_ys = [x[1] for x in pt_coordinates]
pt_xs = [x[0] for x in pt_coordinates]

pt_offset_ys = get_offset_nums(pt_ys, empty_rows)
pt_offset_xs = get_offset_nums(pt_xs, empty_cols)

offset_coords = zip(pt_offset_xs, pt_offset_ys)

path_length_sum = sum(get_paths(offset_coords))

# print(empty_cols)
print(path_length_sum)

# print(pt_offset_xs)
# print("\n".join(["".join(x) for x in part_two_grid]))


