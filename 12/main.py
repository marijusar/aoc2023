f = open("./input.txt")
lines = [x.strip().split(' ') for x in f.readlines()]
possibilities = 0

mem = {}

def calc_substring(springs, groups) :
    if not springs and groups :
        return 0

    if not groups :
        if "#" in springs :
            return 0
        else :
            return 1

    current_spring = springs[0]
    current_group = groups[0]

    def handle_dot() :
        cache_key = springs[1:] + ",".join([str(x) for x in groups])
        mem[cache_key] = calc_substring(springs[1:], groups)
        return mem[cache_key]

    def handle_pound() :
        curr_spring_group = springs[:current_group]
        
        if "?" in curr_spring_group : 
            curr_spring_group = curr_spring_group.replace("?" , "#")

        if curr_spring_group != "#" * current_group :
            return 0 

        if len(springs) == current_group and len(groups) > 1 :
            return 0

        if len(springs) == current_group:
            return 1
        else :
            next_char = springs[current_group]
            if next_char in "?." :
                cache_key = springs[current_group + 1:] + ",".join([str(x) for x in groups[1:]])
                mem[cache_key] = calc_substring(springs[current_group + 1:], groups[1:])
                return mem[cache_key]
            else : 
                return 0



        return 0

    cache_key = springs + ",".join([str(x) for x in groups])

    if cache_key in mem :
        return mem[cache_key]

    if current_spring == "." :
            possibilities = handle_dot()

    if current_spring == "#" :
            possibilities = handle_pound()

    if current_spring == "?" :
        possibilities = handle_dot() + handle_pound()

    return possibilities


def map_lines(x) :
    mapped_lines = []
    for line in x :
        springs, group = line
        group_tuple = [int(x) for x in group.split(",")]
        mapped_lines.append([springs, group_tuple])
    return mapped_lines



unfolded_groups = [",".join(x[1].split(",") * 5) for x in lines]
unfolded_springs = ["?".join(x[0].split() *5) for x in lines]

unfolded_lines = list(zip(unfolded_springs, unfolded_groups))

 
mapped_unfolded_lines = map_lines(unfolded_lines)

 
part_two = sum([calc_substring(*x) for x in map_lines(unfolded_lines)])

print(part_two)
 



