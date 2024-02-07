def part_one() :
    f = open("./input.txt")
    lines = f.readlines()
    input = []
    for line in lines :
        _ , values = line.split(":")
        cols = values.strip().split(" ")
        items = list(map(lambda x: int(x), filter(lambda x: x != "", cols)))
        input.append(items)

    races = list(zip(input[0], input[1]))
    answer = 1

    for race in races :
        win_possibilities = 0
        
        for i in range(0, race[0]) :
            speed = i 
            time_remaining = race[0] - i

            distance_travelled = speed * time_remaining

            if distance_travelled > race[1] :
                win_possibilities += 1
        answer *= win_possibilities
    print(answer)



# part_one()



def part_two() :
    f = open("./input.txt")
    lines = f.readlines()
    input = []
    for line in lines :
        _ , values = line.split(":")
        cols = values.strip().split(" ")
        stripped_kerning = list(filter(lambda x: x != "", cols))
        print(stripped_kerning)
        kerning_value = "".join(stripped_kerning)

        input.append(kerning_value)


    win_possibilities = 0

    int_input = list(map(lambda x: int(x), input))
    
    for i in range(0, int_input[0]) :
        # x(y- x) > 219101213651089
        # where 0 <= x <= 40817772
        speed = i 
        time_remaining = int_input[0] - i

        distance_travelled = speed * time_remaining

        if distance_travelled > int_input[1] :
            win_possibilities += 1

    print(win_possibilities)

part_two()
