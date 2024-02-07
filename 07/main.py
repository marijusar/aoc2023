import functools

f = open("input.txt")
lines = [x.strip().split(" ") for x in f.readlines()]
cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
card_score_index = list(reversed(cards))

def is_two_pair(a) :
    if(max(a) == 2) :
        item_index = a.index(2)
        a.pop(item_index)
        return max(a) == 2
    return False

 
def is_full_house(a) :
    if(max(a)) == 3 :
        item_index = a.index(3)
        a.pop(item_index)
        return max(a) == 2

    return False

def determine_hand_score(a):
    hand = {}
    for char in a :
        if char not in hand :
            hand[char] = 1
            continue

        hand[char] += 1
    hand_counts =list(hand.values())
    hand_max = max(hand_counts)

    if hand_max > 3 :
        return hand_max + 2

    if hand_max == 3 :
        return 5 if is_full_house(hand_counts) else 4

    if hand_max == 2 :
        return 3 if is_two_pair(hand_counts) else 2

    return hand_max


def hand_compare_function(a, b) :
    hand_a_score = determine_hand_score(a[0])
    hand_b_score = determine_hand_score(b[0])

    if hand_a_score != hand_b_score :
        return hand_a_score - hand_b_score

    for i in range(0, len(a[0])) :
        char_a = a[0][i]
        char_b = b[0][i]

        if char_a == char_b:
            continue
        else :
            return card_score_index.index(char_a) - card_score_index.index(char_b)
    
    return 0


def part_one() :
    sorted_lines = sorted(lines, key=functools.cmp_to_key(hand_compare_function))
    acc = 0 

    for i in range(0, len(sorted_lines)) :
        num = int(sorted_lines[i][1]) * (i + 1)
        acc += num

    return acc
        


print(part_one())

    



