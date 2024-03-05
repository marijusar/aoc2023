f = open("./test.txt")
lines = f.readlines()

l = [x.strip().split(":") for x in lines]

a_l = {}

for i in l : 
    a_l[i[0]] = i[1].strip().split(' ')

print(a_l)

