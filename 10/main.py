file = open("test5.txt")
lines = [x.strip() for x in file.readlines()]

class Coordinates :
    def __init__ (self, x, y):
       self.x = x
       self.y = y
    def to_tuple(self) :
        return [self.x, self.y]
class PipeValidator :
    pipe_rules = {
        ## [offset1, offset2]
        "|" : [[0, 1],[0, -1]],
        "-" : [[1, 0],[-1, 0]],
        "L" : [[0, -1],[1, 0]],
        "J" : [[0, -1],[-1, 0]],
        "7" : [[-1, 0],[0, 1]],
        "F" : [[0, 1], [1, 0]]
    }

    def is_pipe(self, pipe_type) :
        pipe_types = self.pipe_rules.keys()
        if pipe_type in pipe_types : 
            return True
        return False

class Pipe :
    def __init__(self, pipe_type, coordinates, validator) :
        self.pipe_type = pipe_type
        self.coordinates = coordinates
        self.validator = validator
    def is_connected_to(self, pipe) :
        pipe_offsets = self.validator.pipe_rules[self.pipe_type]
        for offset in pipe_offsets :
            is_x_same = self.coordinates.x + offset[0] == pipe.coordinates.x
            is_y_same =self.coordinates.y + offset[1] == pipe.coordinates.y
            if  is_x_same and is_y_same:
                return True
        return False
    def get_next_pipe_coordinates(self, connected_pipe) :
        pipe_offsets = self.validator.pipe_rules[self.pipe_type]
        for offset in pipe_offsets :
            is_x_same = self.coordinates.x + offset[0] == connected_pipe.coordinates.x
            is_y_same =self.coordinates.y + offset[1] == connected_pipe.coordinates.y
            if  is_x_same and is_y_same:
                continue
            else :
                return Coordinates(self.coordinates.x + offset[0], self.coordinates.y + offset[1])
        Exception("Should be unreacheable")
    def is_same_pipe(self, pipe) :
        if self.coordinates.x == pipe.coordinates.x and self.coordinates.y == pipe.coordinates.y :
            return True
        return False


class Grid :
    pipe_offsets = [[0, -1], [0, 1], [1, 0], [-1, 0]]
    def __init__(self, grid, pipe_validator) :
        self.grid = grid
        self.pipe_validator = pipe_validator

    def get_starting_point(self) :
        for y, line in enumerate(self.grid) :
            for x,item in enumerate(line) :
                if item == "S" :
                    return Coordinates(x, y)
    
    def look_for_initial_connecting_pipe(self, starting_coordinates) :

        for pipe_offset in self.pipe_offsets :
            new_x = starting_coordinates.x + pipe_offset[0]
            new_y = starting_coordinates.y + pipe_offset [1]

            if self.pipe_validator.is_pipe(self.grid[new_y][new_x]) :
                pipe = Pipe(self.grid[new_y][new_x], Coordinates(new_x, new_y), PipeValidator())
                if pipe.is_connected_to(Pipe("S", starting_coordinates, PipeValidator())) :
                    return Pipe(self.grid[new_y][new_x], Coordinates(new_x, new_y), PipeValidator())
    
    def get_next_pipe(self, current_pipe, prev_pipe) :
        coordinates = current_pipe.get_next_pipe_coordinates(prev_pipe)

        return Pipe(self.grid[coordinates.y][coordinates.x], coordinates, PipeValidator())
    
    def get_nest_start_coordinates(self): 
        for y, lines in enumerate(self.grid) :
            for x, position in enumerate(lines) :
                if position == "." :
                    return Coordinates(x, y)
                    
        

    def mark_coordinates(self, coordinates, char) :
            for coord in coordinates :
                line = self.grid[coord.y] 
                line_array = [x for x in line]
                line_array[coord.x] = char
                replaced_char_string = "".join(line_array)
                self.grid[coord.y] = replaced_char_string

    def ray_cast(self) :
        pipes = ["|", "L", "J" ]
        acc = 0
        for y, line in enumerate(self.grid) :
            for x,char in enumerate(line) :
                intersection_count = 0
                if char == "." :
                    for i in range (x, len(self.grid[0])) :
                        if self.grid[y][i] in pipes :
                            intersection_count += 1
                if intersection_count % 2 == 1 :
                    acc += 1
        return acc


class PipeLoop :
    def __init__(self, grid, pipe_validator) :
        starting_point = grid.get_starting_point()
        connecting_pipe = grid.look_for_initial_connecting_pipe(starting_point)
        starting_pipe = Pipe("S", starting_point, pipe_validator)
        pipe_loop = [starting_pipe, connecting_pipe]

        while not pipe_loop[len(pipe_loop) -1].is_same_pipe(pipe_loop[0]) : 
            next_pipe = grid.get_next_pipe(pipe_loop[len(pipe_loop) -1], pipe_loop[len(pipe_loop) -2])
            pipe_loop.append(next_pipe)

        self.pipe_loop = pipe_loop
        self.grid = grid.grid

    def get_loop(self) :
        return self.pipe_loop

    def get_steps_count() :
        pipe = len(self.pipe_loop) - 1

        mod =  pipe_loop_without_duplicate_initial_pipe % 2

        steps_count = int(pipe_loop_without_duplicate_initial_pipe / 2 + 1 if mod else pipe_loop_without_duplicate_initial_pipe / 2)

        return steps_count

    def get_boundaries(self) :
        x_coords = [x.coordinates.x for x in self.pipe_loop]
        y_coords = [y.coordinates.y for y in self.pipe_loop]
        
        return [Coordinates(min(x_coords), min(y_coords)), Coordinates(min(x_coords), max(y_coords)), Coordinates(max(x_coords), min(y_coords)) , Coordinates(max(x_coords), max(y_coords))]
    
    def remove_unused_pipes(self) :
        grid = Grid(self.grid, PipeValidator())
        for y, line in enumerate(grid.grid) :
            for x, char in enumerate(grid.grid[y]) :
                grid.mark_coordinates([Coordinates(x, y)], ".")

        for pipe in self.pipe_loop :
            grid.mark_coordinates([pipe.coordinates], pipe.pipe_type)
        
        return grid

    

pipe_grid = Grid(lines, PipeValidator())
pipe_loop = PipeLoop(pipe_grid, PipeValidator())
pipe_grid_without_thrash = pipe_loop.remove_unused_pipes().grid
grid_without_thrash = Grid(pipe_grid_without_thrash, PipeValidator())

print()
print("\n".join(grid_without_thrash.grid))
print(grid_without_thrash.ray_cast())
