import re

f = open("./test1.txt")
uppercase_words_regex = re.compile("[A-Z]+(?![a-z])")
instructions, desert_map = f.read().split("\n\n")
desert_map_items = [re.findall(uppercase_words_regex, x) for x in desert_map.split("\n")[0:-1]]
desert_map_dict = {}

for desert_map_item in desert_map_items :
    entry, left, right = desert_map_item
    desert_map_dict[entry] = [left, right]

print(desert_map_dict)

def part_one() :
    count = 0 
    current_position = "AAA"
    instruction_position = 0
    instructions_len = len(instructions)

    while current_position != "ZZZ" :
        if instruction_position == instructions_len :
            instruction_position = 0

        instruction = instructions[instruction_position]
        left, right = desert_map_dict[current_position]

        if instruction == "R" :
            current_position = right

        if instruction == "L" :
            current_position = left


        instruction_position +=1
        count += 1

            

    return count

print(part_one())




