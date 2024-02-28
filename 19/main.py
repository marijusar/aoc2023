import copy

f = open("./input.txt")
i, p = f.read().split("\n\n")

i_a = i.split("\n")
p_a = [x for x in p.split("\n") if x != ""]

instructions = {}
parts = []

for i in i_a :
    x, v= i.split("{")
    instructions[x] = [x for x in v[:-1].split(",") if x != ""]

for i in p_a :
    pp = i[1:-1].split(",")
    acc = {}

    for j in pp :
        acc[j[0]] =  int(j[2:])

    parts.append(acc)



def solve(part, instruction):
    if instruction == "R" :
        return 0 
   
    if instruction == "A" :
        return sum(list(part.values()))

    instruction_set = instructions[instruction] 

    for i in instruction_set :
        if i == "R" :
                return 0 
           
        if i == "A" :
                return sum(list(part.values()))

        if i in instructions :
            return solve(part, i)

        condition, next = i.split(":")
        symbol = condition[0]
        operator = condition[1]
        value = condition[2:]

        if operator == ">" :
            if part[symbol] > int(value)  :
                return solve(part, next)

        if operator == "<" :
            if part[symbol] < int(value) :
                return solve(part, next)



part_one = sum([solve(part, "in") for part in parts])
print(part_one)

def split_range(r,s, o, v) :
    r_cp_t = copy.deepcopy(r)
    r_cp_f = copy.deepcopy(r)
    min, max = r[s]

    if o == "<" :
        r_cp_t[s] = (min, v - 1)
        r_cp_f[s] = (v, max)
        return (r_cp_t, r_cp_f)

    if o == ">" :
        r_cp_t[s] = (v + 1, max)
        r_cp_f[s] = (min, v)
        return (r_cp_t, r_cp_f)


def solve_ranges(instruction, ranges):
    positions = [(instruction, ranges)]
    r_a = []
    

    while len(positions) > 0 :
        p = positions.pop(0)
        i, r = p
        temp_r = r


        if i == "R" :
            continue

        if i == "A" :
            r_a.append(temp_r)
            continue

        instruction_set = instructions[i]
        for idx, j in enumerate(instruction_set) :
            if j == "R" :
                continue

            if j == "A" :
                r_a.append(temp_r)
                continue

            if j in instructions :
                positions.append((j, temp_r))
                continue

            condition, next = j.split(":")
            symbol = condition[0]
            operator = condition[1]
            value = int(condition[2:])

            rs = split_range(temp_r, symbol , operator, value) 


            if not rs :
                continue

            t, f = rs
            

            temp_r = f


            positions.append((next, t))
    return r_a


acc = {
    "x" : (1, 4000),
    "m" : (1, 4000),
    "a" : (1, 4000),
    "s" : (1, 4000)
}

ranges = solve_ranges("in", acc)

def get_possibilities(r):
    u = [x for x in list(r.values())]
    acc = 1
    
    for j in u :
        l = j[1] - j[0] + 1
        acc = acc * l

    return acc

p2 = sum([get_possibilities(x) for x in ranges])
print(f'{p2:,}')



