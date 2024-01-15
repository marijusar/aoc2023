
limits = {
        "red" : 12,
        "green" : 13,
        "blue" :14
        }

def main(): 
    f = open("./input.txt")   
    lines = f.readlines();
    acc = 0

    for idx, game in enumerate(lines):
        if game is None :
            continue
        if game == "\n" :
            continue

        suf = [x for x in game.split(":") if len(x) > 1 ]
        shows =  [x.strip() for x in suf[1].replace(";", ",").split(",")]
        print(shows)
        hasHigher = False

        for show in shows : 
            number, color  = show.split(" ")

            if limits[color] < int(number) : 
                # print({"color" : color, "number" : number})
                hasHigher = True
        
        if hasHigher is False :
            print(idx + 1)
            acc += idx + 1
            # print(acc)


        hasHigher = False
        
    print(acc)



main()
