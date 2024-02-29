import copy

f = open("./input.txt")
lines = [x.strip().split(" ") for x in f.readlines()]

def print_grid(grid): 
    print("\n".join(["".join(x) for x in grid]))


direction_map = {
    "R" : [1, 0],
    "D" : [0, 1],
    "L" : [-1, 0],
    "U" : [0, -1]
}

def create_coordinates(lines) :
    cursor = [-1, 0]
    coordinates = []
    for line in lines :
        direction, distance, _ = line 
        x, y = cursor
        new_x, new_y = x + direction_map[direction][0] * int(distance), y + direction_map[direction][1] * int(distance)
        cursor = [new_x, new_y]
        coordinates.append(cursor)

    max_x = max(x[0] for x in coordinates)
    max_y = max(x[1] for x in coordinates)
    perimeter = sum([int(x[1]) for x in lines])
    
    return coordinates, max_x, max_y, perimeter

coordinates, max_x, max_y, perimeter = create_coordinates(lines)

def solve_shoelace(coordinates, perimeter) :
    acc = 0
    for i in range(0, len(coordinates)) : 
        if i == len(coordinates) - 1 :
            acc+= coordinates[i][0] * coordinates[0][1] - coordinates[0][0] * coordinates[i][1]
            return int(abs(acc) / 2) + int(perimeter / 2) + 1
 
        acc += coordinates[i][0] * coordinates[i + 1][1] - coordinates[i + 1][0] * coordinates[i][1]

part_one = solve_shoelace(coordinates, perimeter)

def create_grid(max_x, max_y, coordinates) :
    grid = [] 
    for _ in range(max_y +1) :
        row = []
        for _ in range(max_x + 1) :
            row.append(".")
        grid.append(row)

    for coordinate in coordinates :
        x, y = coordinate
        grid[y][x] = "#"
    return grid

# grid = create_grid(max_x, max_y, coordinates)

def solve(grid) :
    answer = 0

    cp_grid = copy.deepcopy(grid)

    for y, row in enumerate(grid) :
        is_inside_polygon = False
        for x, item in enumerate(row) :
            if y - 1 < 0 : continue
            if item == "#"  and grid[y-1][x] == "#":
                is_inside_polygon = not is_inside_polygon

            if item == "." and is_inside_polygon == True :
                cp_grid[y][x] = "#"



    for row in cp_grid :
        for item in row :
            if item == "#" :
                answer += 1

    return answer
    
# part_one = solve(grid)

def decode_hexadecimal(lines) :
    hex_direction_map = {
        "0" : "R",
        "1" : "D",
        "2"  : "L",
        "3" : "U"
    }
    decoded = []
    for line in lines :
        _, _, hex = line 
        hex_trimmed = hex.replace(")", "").replace("(", "").replace("#", "")
        direction = hex_direction_map[hex_trimmed[len(hex_trimmed) - 1]]
        distance = int(hex_trimmed[0:len(hex_trimmed) - 1], 16)

        decoded.append([direction, distance, hex])
    return decoded

hex_lines = decode_hexadecimal(lines)
coordinates, _ , _, perimeter  = create_coordinates(hex_lines)

part_two = solve_shoelace(coordinates, perimeter)

print(part_two)

