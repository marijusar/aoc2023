import copy

f = open("./input.txt")
grid = [[y for y in x.strip()] for x in f.readlines()]



beam_direction_map = {
    "w" : (-1 , 0),
    "e" : (1 , 0),
    "s" : (0 , 1),
    "n" : (0 , -1)
}

def get_beam_direction(beam) :
    current_tile, next_tile = beam
    curr_x, curr_y = current_tile
    next_x, next_y = next_tile

    if curr_x < next_x :
        return "e"
    if curr_x > next_x :
        return "w"
    if next_y > curr_y :
        return "s"
    if next_y < curr_y :
        return "n"


def solve(start) :
    cp = copy.deepcopy(grid)
    energized = []
    beams = [start]
    beam_starts = []
    while len(beams) > 0:
        beam = beams.pop(0)
        current_tile, next_tile = beam
        x_next, y_next = next_tile
        direction = get_beam_direction(beam)

        if ((x_next, y_next)) in beam_starts :
            continue

        if x_next < 0 or x_next >= len(cp[0]) or y_next < 0 or y_next >= len(cp) :
            continue
     

        energized.append((x_next, y_next, direction))

        if cp[y_next][x_next] == "|" and (direction == "e" or direction == "w") :
            beams.append(((x_next, y_next), (x_next, y_next + 1 )))
            beam_starts.append((x_next, y_next))
            beams.append(((x_next, y_next), (x_next, y_next - 1 )))

        elif cp[y_next][x_next] == "-" and (direction == "n" or direction == "s") :
            beams.append(((x_next, y_next), (x_next + 1, y_next )))
            beams.append(((x_next, y_next), (x_next - 1, y_next )))
            beam_starts.append((x_next, y_next))

        elif cp[y_next][x_next] == "/" :
            if direction == "s" :
                beams.append(((x_next, y_next), (x_next - 1, y_next)))
            if direction == "n" :
                beams.append(((x_next, y_next), (x_next + 1, y_next)))
            if direction == "e" :
                beams.append(((x_next, y_next), (x_next, y_next - 1)))
            if direction == "w" :
                beams.append(((x_next, y_next), (x_next, y_next + 1)))

        elif cp[y_next][x_next] == '\\' :
            if direction == "s" :
                beams.append(((x_next, y_next), (x_next + 1, y_next)))
            if direction == "n" :
                beams.append(((x_next, y_next), (x_next - 1, y_next)))
            if direction == "e" :
                beams.append(((x_next, y_next), (x_next, y_next + 1)))
            if direction == "w" :
                beams.append(((x_next, y_next), (x_next, y_next - 1)))
        else :
            x_beam_offset, y_beam_offset = beam_direction_map[direction]
            beams.append(((x_next, y_next), (x_beam_offset + x_next , y_beam_offset + y_next)))

    for i in energized : 
        cp[i[1]][i[0]] = "#"


    return sum([x.count("#") for x in cp])

part_one = solve(((-1,0), (0,0)))
print(part_one)

solutions = []

for y_idx, y in enumerate(grid) :
    left_to_right = solve(((-1, y_idx), (0, y_idx)))
    right_to_left = solve(((len(grid[y_idx]), y_idx), (len(grid[y_idx]) - 1, y_idx)))
    solutions.append(left_to_right)
    solutions.append(right_to_left)

for x_index , x in enumerate(grid[0]) :
    top_to_bottom = solve(((x_index, -1), (x_index, 0)))
    bottom_to_top = solve(((x_index, len(grid[0])), (x_index, len(grid[0]) - 1)))
    solutions.append(top_to_bottom)
    solutions.append(bottom_to_top)


part_two = max(solutions)
print(part_two)

