import re

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

boxes = {}
label_re=re.compile('^[^=|-]*')
nums_re = re.compile("[0-9]")

for i in range(0, len(sequence)) :
    item = sequence[i]
    label = label_re.findall(item)[0]
    box_num = hash(label)
    focal_length = item[len(item) - 1]

    if "=" in item :
        if box_num not in boxes :
            boxes[box_num] = {"labels" : [label], "focal_lengths" : [focal_length]}
        else :
            if label in boxes[box_num]["labels"] :
                label_index = boxes[box_num]["labels"].index(label)
                boxes[box_num]["focal_lengths"][label_index] = focal_length

            if label not in boxes[box_num]["labels"] :
                boxes[box_num]["labels"].append(label)
                boxes[box_num]["focal_lengths"].append(focal_length)

    if "-" in item :
        if box_num not in boxes : 
            continue
        if label in boxes[box_num]["labels"] :
            label_index = boxes[box_num]["labels"].index(label)
            boxes[box_num]["labels"].pop(label_index)
            boxes[box_num]["focal_lengths"].pop(label_index)

    if len(boxes[box_num]["labels"]) == 0 :
        boxes.pop(box_num)


part_two = 0

for box in list(boxes.keys()) :
    for idx, i in enumerate(boxes[box]["focal_lengths"]) :
        part_two += (idx + 1) * (int(box) + 1) * int(i)

    

print(part_two)
