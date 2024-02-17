f = open("./input.txt")
patterns = [x.split("\n") for x in f.read().strip().split("\n\n")]


def find_string_diff_count(a,b) :
    cnt = 0
    for i in range(0, len(a)) :
        if a[i] != b[i] :
            cnt += 1
    return cnt

def check_reflection(pattern, reflect_point):
    for j in range(0, reflect_point + 1) :
        next_index = reflect_point + j + 1
        prev_index = reflect_point - j
        if next_index >= len(pattern) or prev_index < 0 :
            continue
        if pattern[prev_index] != pattern[next_index] :
            return False

    return True

def check_reflection_with_smudge(pattern, reflect_point):
    for j in range(0, reflect_point + 1) :
        next_index = reflect_point + j + 1
        prev_index = reflect_point - j
        if next_index >= len(pattern) or prev_index < 0 :
            continue
        if pattern[prev_index] != pattern[next_index] and find_string_diff_count(pattern[prev_index], pattern[next_index]) != 1 :
            return False

    return True

def is_horizontal_reflection_with_smudge(pattern, item, cache) :
    for i in range(0, len(pattern)) :
        if i + 1 >= len(pattern) :
            continue
        if pattern[i] == pattern[i+1] or find_string_diff_count(pattern[i], pattern[i+1]) == 1:
            if item in cache and cache[item] == i + 1 :
                continue
            if check_reflection_with_smudge(pattern, i) :
                return i + 1
    return None

def is_horizontal_reflection(pattern) :
    for i in range(0, len(pattern)) :
        if i + 1 >= len(pattern) :
            continue
        if pattern[i] == pattern[i+1] :
            if check_reflection(pattern, i) :
                return i + 1
    return None

def is_vertical_reflection_with_smudge(pattern, item, cache) :
    row_arrays = [list(x) for x in pattern]
    columns =  list(zip(*row_arrays))

    return is_horizontal_reflection_with_smudge(columns, item, cache)

def is_vertical_reflection(pattern) :
    row_arrays = [list(x) for x in pattern]
    columns =  list(zip(*row_arrays))

    return is_horizontal_reflection(columns)



# horizontal_reflections = [is_horizontal_reflection(x) * 100 for x in patterns if is_horizontal_reflection(x)]
# vertical_reflections = [is_vertical_reflection(x) for x in patterns if is_vertical_reflection(x)]
#
# part_one = sum(horizontal_reflections + vertical_reflections)
#
# print(part_one)


# P2
# 1. Loop over patterns
# 2. Find new possible reflection line 
# 3. Check if reflection is possible. When running check_relflection, account for cases when find_string_diff_count == 1
# 4. If no possible reflection lines are found, maybe reflection line has a smudge , therefore try finding new reflection line with smudge


# Cache old reflection lines

v_mem = {}
h_mem = {}
for i in range(0,len(patterns)) :
    horizontal_reflection = is_horizontal_reflection(patterns[i])

    if horizontal_reflection : 
        h_mem[i] = horizontal_reflection

    vertical_reflection = is_vertical_reflection(patterns[i])

    if vertical_reflection :
        v_mem[i] = vertical_reflection


part_two = 0

for i in range(0, len(patterns)) :
    is_horizontal = is_horizontal_reflection_with_smudge(patterns[i], i, h_mem)
    if is_horizontal :
        part_two += is_horizontal * 100


    is_vertical = is_vertical_reflection_with_smudge(patterns[i],i , v_mem)
    if is_vertical :
        part_two += is_vertical

print(part_two)


