from copy import deepcopy
from functools import cmp_to_key
f = open("./input.txt")
lines = f.readlines()

def print_grid(grid) :
    print( "\n".join(["".join(x) for x in reversed(grid)]))
    print("------")

s = [x.strip().split("~") for x in lines]
c = []

max_x = 0
max_y = 0
max_z = 0

def sort_by_start_z(a, b) :
    start_a, _ = a
    start_b, _ = b
    return start_a[2] - start_b[2]


for i in s :
    acc = []
    for j in i :
        k = tuple([int(x) for x in j.split(",")])
        x, y, z = k 
        if x > max_x :
            max_x = x
        if y > max_y :
            max_y = y
        if z > max_z : 
            max_z = z
        acc.append(k)
    c.append(acc)

c = list(sorted(c, key=cmp_to_key(sort_by_start_z)))

def get_range_points(l) :
    start, end = l
    start_x, start_y, _ = start
    end_x, end_y , _ = end
    acc = [(start_x, start_y), (end_x, end_y)]

    for i in range(0 , end_x - start_x) :
        acc.append((start_x + i, start_y))

    for i in range(0, end_y - start_y) :
        acc.append((start_x, start_y + i))

    return list(set(acc))


def lines_intersecting(l1, l2) :
    p_1 = get_range_points(l1)
    p_2 = get_range_points(l2)
    for i in p_1 :
        if i in p_2 :
            return True
    return False

print(lines_intersecting(((2, 0, 2), (2, 0, 2)), ((2, 0, 0), (2, 0, 0))))

def calc_z_offset(brick, l):
    start, end = brick
    start_x, start_y, start_z = start
    end_x, end_y, end_z  = end

    new_start_z = start_z

    for z in range(start_z - 1, -1, -1) :
        intersecting_zs=  [x for x in l if x[0][2] <= z and x[1][2] >= z]
        if len(intersecting_zs) == 0 :
            new_start_z = z

        for j in intersecting_zs : 
            if lines_intersecting(brick, j):
                offset = start_z - new_start_z 
                if brick == [(2, 0, 2), (2, 0, 2)] :
                        print(new_start_z)
                return offset
        new_start_z = z

    offset = start_z - new_start_z 

    return offset

# print(c)
def calc_new_coords(coords, k) :
    is_offsetting = False
    cnt = 0
    # print(coords)
    for i in range(0, len(coords)) :
        start, end = coords[i]
        start_x, start_y, start_z = start
        end_x, end_y, end_z  = end

        o = calc_z_offset(coords[i], coords)

        if o > 0 and k:
            cnt += 1
            is_offsetting = True


        new_start_z = start_z - o if start_z - o > 0 else 0
        new_end_z = end_z - o if start_z - o > 0 else  end_z - start_z 

        p = [(start_x, start_y, new_start_z), (end_x, end_y, new_end_z)]

        coords[i] = p
    if k :
        return (is_offsetting, cnt)

    return coords


def create_list(x, y) :
    acc = []
    for y in range(0, y + 1) : 
        l = []
        for x in range(0,  x +1) : 
            l.append(".")
        acc.append(l)

    return acc




def print_y_grid(c) :
    y_grid = create_list(max_y, max_z)
    for idx, i in enumerate(c) :
        start, end = i
        _, start_y, start_z = start
        _, end_y, end_z = end

        for z in range(start_z, end_z + 1) :
            for y in range(start_y, end_y + 1) :
                if y_grid[z][y] != "." : 
                    y_grid[z][y] = "?"
                    continue
                y_grid[z][y] = chr(ord("A") + idx)
    print_grid(y_grid)

def print_x_grid(c) :
    x_grid = create_list(max_x, max_z)
    for idx, i in enumerate(c) :
        start, end = i
        start_x, _, start_z = start
        end_x, _, end_z = end

        for z in range(start_z, end_z + 1) :
            for x in range(start_x, end_x + 1 ) :
                if x_grid[z][x] != "." : 
                    x_grid[z][x] = "?"
                    continue
                x_grid[z][x] = chr(ord("A") + idx)
    print_grid(x_grid)

n_g = calc_new_coords(deepcopy(c), False)
print_x_grid(n_g)
print_y_grid(n_g)

part_one = 0 
part_two = 0

for i in range(len(c)) :
     print(i)
     s = deepcopy(n_g)
     k = s.pop(i)
     r, p = calc_new_coords(s, True)

     if r == False :
         part_one += 1
     part_two += p   

print(part_two)
