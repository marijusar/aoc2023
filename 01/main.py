import re

numWordDic = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4, 
        "five" : 5,
        "six" : 6,
        "seven" : 7, 
        "eight" : 8, 
        "nine" : 9
        }

def main(): 
    f = open("./input.txt")
    numre = re.compile("(?=([\d]|one|two|three|four|five|six|seven|eight|nine))")
    lines = f.readlines()
    acc = 0

    for line in lines: 
        search = numre.search(line)
        
        if search is not None :
            print(line.lstrip())
            nums = numre.findall(line.lstrip())
            print(nums)
            first = str(numWordDic[nums[0]]) if nums[0] in numWordDic else str(nums[0])
            last = str(numWordDic[nums[len(nums) - 1]]) if nums[len(nums)- 1] in numWordDic else str(nums[len(nums) - 1])

            number = first + last

            print(number)
                

            acc += int(number)

    print(acc)


main()
