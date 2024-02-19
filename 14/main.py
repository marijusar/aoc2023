f = open("./input.txt")
lines = [x.strip() for x in f.readlines()]
columns = list(zip(*lines))

def get_first_empty_index(col, start_at) :
    for idx, i in enumerate(col):
        if idx < start_at :
            continue
        if i == "." :
            return idx
    


def move_columns(columns) :
    blocker_index = None
    empty_space_index = None
    
    for idx, item in enumerate(columns) :
        if item == "O" :
            if empty_space_index is None:
                continue
            else :
                if not blocker_index or empty_space_index > blocker_index :
                    columns[empty_space_index] = "O"
                    columns[idx] = "."
                    empty_space_index = get_first_empty_index(columns, blocker_index) if blocker_index else get_first_empty_index(columns, 0) 

        if item == "#" :
            blocker_index = idx 

        if item == "." :
            if empty_space_index is None:
                empty_space_index = idx
            if blocker_index and empty_space_index < blocker_index:
                empty_space_index = idx

    return columns

def calculate_column_load(col) :
    acc = 0 
    for idx, i in enumerate(col) :
        if i == "O" :
            acc += len(col) - idx

    return acc


def print_grid(grid) :
    print("\n".join(["".join(x) for x in grid]))

def serialize_grid(grid) :
    return "\n".join(["".join(x) for x in grid])

def iterate(grid) :
    columns = [list(x) for x in zip(*grid)]
    moved_columns = [move_columns(x) for x in columns]
    rows = [x for x in list(zip(*moved_columns))]
    moved_rows = [move_columns(list(x)) for x in rows]
    columns_again = [list(reversed(x)) for x in list(zip(*moved_rows))]
    moved_reversed_columns = [move_columns(x) for x in columns_again]
    unreversed_columns = [list(reversed(x)) for x in moved_reversed_columns]
    reversed_rows = [list(reversed(x)) for x in list(zip(*unreversed_columns))]
    moved_reversed_rows = [move_columns(x) for x in reversed_rows]
    unreverse_rows = [list(reversed(x)) for x in moved_reversed_rows]
    return unreverse_rows


mem = {}
times = 1000000000

def iterate_times(grid, times) :
    temp_grid = grid
    first_loop = True
    first_index = None
    serialized_repeater_grid = None
    for i in range(0, times) :
        temp_grid = iterate(temp_grid)
        serialized_grid = serialize_grid(temp_grid)
        
        if serialized_grid in mem and first_loop :
            mem[serialized_grid] = i
            serialized_repeater_grid = serialized_grid
            first_loop = False
            first_index = i
        elif serialized_grid == serialized_repeater_grid and not first_loop :
            return [i, first_index ]
        else :
            mem[serialized_grid] = i
 
second_time, first_time = iterate_times(lines, times) 
print(second_time, first_time)
looping_gens = times - first_time 
in_loop_gens = looping_gens % (second_time - first_time)

mem_key =list({i for i in mem if mem[i]== first_time - 1 + in_loop_gens})
rows = mem_key[0].split("\n")

part_two = sum([calculate_column_load(x) for x in zip(*rows)])
print(part_two)



