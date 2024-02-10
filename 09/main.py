f = open("./input.txt")
lines = [[int(y.strip()) for y in x.split(" ")] for x in f.readlines()]

def extrapolate_number(a) :
    if all(x == 0 for x in a ) :
        return 0
    new_numbers = []
    for i in range (0, len(a) - 1) :
        diff = a[i + 1] - a[i]
        new_numbers.append(diff)

    return a[len(a) - 1] + extrapolate_number(new_numbers)

def extrapolate_number_backwards(a) :
    if all(x == 0 for x in a) :
        return 0
    new_numbers = []
    for i in range (0, len(a) - 1) :
        diff = a[i + 1] - a[i]
        new_numbers.append(diff)

    return a[0] - extrapolate_number_backwards(new_numbers)



def part_one() :
    numbers = [extrapolate_number(x) for x in lines]
    total = sum(numbers)
    
    return total

# print(part_one())

    

def part_two() :
    numbers = [extrapolate_number_backwards(x) for x in lines]
    total = sum(numbers)
    
    return total

print(part_two())

