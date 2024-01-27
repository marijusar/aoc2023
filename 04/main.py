def part_one() :
    f = open("./input.txt")
    lines = [x.strip() for x in f.readlines()]
    acc = 0
    
    for line in lines :
        pref, data = line.split(":")
        winning_nums_str, card_nums_str = data.split("|")

        winning_nums = winning_nums_str.strip().split(" ")
        # O(1) access rather than extra loop to check every number
        winning_nums_map = {}
        for winning_num in winning_nums :
            winning_nums_map[winning_num] = True
        
        card_nums = card_nums_str.strip().split(" ")
        card_winning_nums = []

        for card_num in card_nums :
            if card_num in winning_nums_map and card_num.isdigit() :
                card_winning_nums.append(card_num)

        acc += pow(2, len(card_winning_nums) - 1) if len(card_winning_nums) > 0 else 0


    print(acc)



# part_one()


def part_two() :
    f = open("./input.txt")
    lines = [x.strip() for x in f.readlines()]
    card_outcome_map = {}
    card_collection_map = {}
    acc = 0

    for idx, card in enumerate(lines) :
        pref, data = card.split(":")
        winning_nums_str, card_nums_str = data.split("|")
        card_nums = list(filter(lambda x: x.isdigit() , card_nums_str.strip().split(" ")))
        winning_nums = list(filter(lambda x: x.isdigit() , winning_nums_str.strip().split(" ")))
        winning_num_map = {}
        acc = 0 

        for num in winning_nums :
            winning_num_map[num] = True

        for num in card_nums :
            if num in winning_num_map :
                acc += 1


        # map to store card outcomes so we can refer which card wins which cards
        card_outcome_map[idx + 1] = list(range(idx +2, idx+ acc + 2))
        # map to track how many of each cards we have
        card_collection_map[idx + 1] = 1

    


    for key in card_outcome_map :
        for won_card in card_outcome_map[key] :
            # I'll pat myself on a back for this, since it's pretty good performance-wise
            # Amount of cards X we get in the end is the initial amount (1) + the amount of cards Y that has won the card X;
            # Example if we have 1 of #1 card and it wins cards #2,#3 we have 2 cards #2 and 2 cards of #3. Now card #2 wins card #3 and #4
            # Now we have 3 cards #3 and 3 cards #4, etc.
            card_collection_map[won_card] += card_collection_map[key]

    acc = 0

    for key in card_collection_map:
        # Once we know how many of each card we have in the end, we just have to add the numbers
        acc += card_collection_map[key]


    print(acc)



    
part_two()
