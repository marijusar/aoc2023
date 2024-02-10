import re

f = open("./input.txt")
uppercase_words_regex = re.compile("[0-9A-Z]+(?![0-9a-z])")
instructions, desert_map = f.read().split("\n\n")
desert_map_items = [re.findall(uppercase_words_regex, x) for x in desert_map.split("\n")[0:-1]]
desert_map_dict = {}

for desert_map_item in desert_map_items :
    entry, left, right = desert_map_item
    desert_map_dict[entry] = [left, right]

def part_one() :
    current_position = "AAA"
    count = 0 
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

a_end = re.compile("\w*A$")
z_end = re.compile("\w*Z$")

keys_that_end_with_a = list(filter(lambda x: re.match(a_end, x), desert_map_dict.keys()))
keys_that_end_with_z = list(filter(lambda x: re.match(z_end, x), desert_map_dict.keys()))

def path_count(start_point, end_point_re) :
    current_position = start_point
    count = 0 
    instruction_position = 0
    instructions_len = len(instructions)


    while re.match(end_point_re, current_position) == None:
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


def gcd(a, b):
    # Euclidian algorhitm. 
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    # Least common multiple
    return a * b // gcd(a, b)

def lcms(a)  :
    if(len(a)) == 1 :
        return a[0]

    z = lcm(a[0], a[1])

    return lcms([z] + a[2:])



def part_two():

    path_counts = [path_count(x, z_end) for x in keys_that_end_with_a]
    count = lcms(path_counts)

    return count


   
print(f'{part_two():,}') 

