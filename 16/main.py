f = open("./test.txt")
grid = [[y for y in x.strip()] for x in f.readlines()]


energized = []
beams = [((0,0), (1, 0))]

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


while len(beams) > 0 :
    beam = beams.pop(0)
    current_tile, next_tile = beam
    x_next, y_next = next_tile
    direction = get_beam_direction(beam)

    if ((current_tile[0], current_tile[1], direction)) in energized :
        continue


    energized.append((current_tile[0], current_tile[1], direction))
    if x_next < 0 or x_next >= len(grid[0]) or y_next < 0 or y_next >= len(grid) :
        continue
 
    print(current_tile, next_tile)
    print(direction)

    if grid[y_next][x_next] == "|" and (direction == "e" or direction == "w") :
        beams.append(((x_next, y_next), (x_next, y_next + 1 )))
        beams.append(((x_next, y_next), (x_next, y_next - 1 )))

    elif grid[y_next][x_next] == "-" and (direction == "n" or direction == "s") :
        beams.append(((x_next, y_next), (x_next + 1, y_next )))
        beams.append(((x_next, y_next), (x_next - 1, y_next )))

    elif grid[y_next][x_next] == "/" :
        if direction == "s" :
            beams.append(((x_next, y_next), (x_next - 1, y_next)))
        if direction == "n" :
            beams.append(((x_next, y_next), (x_next + 1, y_next)))
        if direction == "e" :
            beams.append(((x_next, y_next), (x_next, y_next - 1)))
        if direction == "w" :
            beams.append(((x_next, y_next), (x_next, y_next + 1)))

    elif grid[y_next][x_next] == '\\' :
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


print(energized)

for i in energized : 
    grid[i[1]][i[0]] = "#"

print("\n".join(["".join(x) for x in grid]))
