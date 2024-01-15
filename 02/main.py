
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

        colorCubeMap = {}

        for show in shows :
            num, color = show.split(" ")
            if color in colorCubeMap :
                if colorCubeMap[color] < int(num) :
                    colorCubeMap[color] = int(num)
            else :
                colorCubeMap[color] = int(num)

        cubeCountArray = colorCubeMap.values()
        cubePowerAccumulator = 1

        print(cubeCountArray)
        
        for c in cubeCountArray : 
           cubePowerAccumulator = c * cubePowerAccumulator 

        acc += cubePowerAccumulator

        
    print(acc)



main()
