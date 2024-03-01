f = open("./input.txt")
grid = [list(x.strip()) for x in f.readlines()]

def print_grid(grid) :
    print("\n".join(["".join(x) for x in grid]))

positions = []
rocks = {}


for y,row in enumerate(grid):
    for x,cell in enumerate(row) :
        if cell == "S" :
            start = ((x, y), (0, 0))
            positions.append(start)
        if cell == "#" : 
            k = ((x,y))
            rocks[k] = True



offsets = [(1,0), (-1, 0), (0, 1), (0,-1)]

def calc_cell_grid_position(p, offset) :
        cell_position, grid_position = p 
        x , y = cell_position
        grid_x, grid_y = grid_position
        new_x,new_y = ((x + offset[0], y + offset[1]))
        if new_x == - 1 :
            return ((len(grid[y]) - 1, new_y), (grid_x - 1, grid_y))
        elif new_x == len(grid[y]) :
            return ((0, new_y), (grid_x + 1, grid_y))
        elif new_y == -1 :
            return ((new_x, len(grid) - 1), (grid_x, grid_y - 1))
        elif new_y == len(grid) :
            return ((new_x, 0), (grid_x, grid_y + 1))

        return ((new_x, new_y), (grid_x, grid_y))


def calc_goal_steps(goal, positions) :
    for _ in range(goal) :
        acc = []
        for i in positions :
            for j in offsets :
                c = calc_cell_grid_position(i, j)
                if c[0] not in rocks :
                    acc.append(c)

        positions = acc
        positions = list(set(positions))

    gardens = []


    for i in positions :
        for j in offsets:
            c = calc_cell_grid_position(i, j)
            if c[0] in rocks :
                continue
            if c in positions :
                continue
            gardens.append(i)

    return len(list(set(gardens)))

# goals = [65, 196, 327]
# part_two = [calc_goal_steps(x, positions) for x in goals]
# print(part_two)
counts = [3738, 33270, 92194]
def difference_table(a) :
    if all(x == 0 for x in a ) :
        return 0
    new_numbers = []
    for i in range (0, len(a) - 1) :
        diff = a[i + 1] - a[i]
        new_numbers.append(diff)

    return a[len(a) - 1] + difference_table(new_numbers)

cnt = len(counts)

while cnt < 202301 :
    if len(counts) > 3 :
        counts.pop(0)
    n = difference_table(counts)
    cnt += 1
    counts.append(n)

part_two = counts[len(counts) - 1]
print(part_two)










# 32644
