f = open("./input.txt")
sequence = [x for x in f.read().strip().split(",")]

def hash(str) :
    acc = 0
    for char in str :
        ascii_char = ord(char)
        acc += ascii_char
        acc *= 17
        acc = acc % 256
    return acc

part_one = sum([hash(x) for x in sequence])
print(part_one)
