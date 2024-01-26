import re

lookaround_coords = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def look_around_for_regexp(x, y, grid, target_reg_exp): 

    for lookaround_coord in lookaround_coords :
        lookaround_x, lookaround_y = lookaround_coord
        lookup_x = x + lookaround_x
        lookup_y = y + lookaround_y

        if lookup_x < 0 or lookup_y < 0 :
            continue

        if lookup_y >= len(grid) : 
            continue

        if lookup_x >= len(grid[y]) :
            continue

        if target_reg_exp.match(grid[lookup_y][lookup_x]) :
            return True
        
    return False

def look_around_for_coords(x, y , grid, target_reg_exp) :
    coords = []
    for lookaround_coord in lookaround_coords :
        lookaround_x, lookaround_y = lookaround_coord
        lookup_x = x + lookaround_x
        lookup_y = y + lookaround_y

        if lookup_x < 0 or lookup_y < 0 :
            continue

        if lookup_y >= len(grid) : 
            continue

        if lookup_x >= len(grid[y]) :
            continue

        if target_reg_exp.match(grid[lookup_y][lookup_x]) :
            coords.append([lookup_x, lookup_y])
    return coords

def part_one() :
    f = open("./input.txt")
    lines = [x.strip() for x in f.readlines()]
    num_re = re.compile("\d")
    symbol_re = re.compile("[^\w.]|_")

    nums = [{"value" : "0", "is_part_num" : False}]

    for line_index, line in enumerate(lines) :
        for char_index, char in enumerate(line) :
            is_num = num_re.match(char)
            is_prev_char_num = num_re.match(lines[line_index][char_index - 1])

            if is_num :
                is_part_num = look_around_for_regexp(char_index, line_index, lines, symbol_re)

                if is_prev_char_num and is_num :
                    last_item = nums[len(nums) - 1] if len(nums) >0 else None
                    last_item["value"] = last_item["value"] + char
                    last_item["is_part_num"] = True if last_item["is_part_num"] else is_part_num
                else : 
                    nums.append({"value" : char, "is_part_num" : is_part_num})
            
    acc = 0 
    for x in nums : 
        if x["is_part_num"] :
            acc += int(x["value"])

    print(acc)


def find_full_number_at_position(grid, x, y) :
        num_re = re.compile("\d")
        
        acc = [grid[y][x]]
        
        left_pointer = x - 1
        right_pointer= x + 1
        left_pointer_end = False
        right_pointer_end = False

        while(left_pointer_end is False or right_pointer_end is False) :

            if left_pointer < 0 :
                left_pointer_end = True

            if right_pointer >= len(grid[y]) :
                right_pointer_end = True

            if right_pointer_end is False :
                if num_re.match(grid[y][right_pointer]) is None :
                    right_pointer_end = True
                    continue

                acc.append(grid[y][right_pointer])
                right_pointer = right_pointer + 1

            if left_pointer_end is False :
                if num_re.match(grid[y][left_pointer]) is None :
                    left_pointer_end = True
                    continue

                acc.insert(0, grid[y][left_pointer])
                left_pointer = left_pointer - 1 
    


        # We will use coordinates in format x1y2x2y2 to deduplicate numbers which have more than 2 digits overlapping with a *.
        return {"value" : int("".join(acc)), "coordinates" : str(left_pointer) + str(y) + str(right_pointer) + str(y)}




def part_two():
    f = open("input.txt")
    lines = [x.strip() for x in f.readlines()]
    star_re = re.compile("\*")
    num_re = re.compile("\d")

    gear_ratio_acc = 0

    for y, line in enumerate(lines) :
        for x,char in enumerate(line) :
            if star_re.match(char):
                num_coords = look_around_for_coords(x, y, lines, num_re)
                nums_acc = []

                for coord in num_coords :
                    num = find_full_number_at_position(lines, coord[0], coord[1])
                    nums_acc.append(num)

                unique_nums = {}

                for num in nums_acc : 
                    unique_nums[num["coordinates"]] = num["value"]

                unique_nums_values = list(unique_nums.values())
                
                if len(unique_nums_values) == 2:
                    print(unique_nums_values)
                    gear_ratio_acc = gear_ratio_acc + (unique_nums_values[0] * unique_nums_values[1])

                
    print(gear_ratio_acc)



part_one()
