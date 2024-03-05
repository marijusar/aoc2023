from copy import deepcopy
import networkx as nx 
import matplotlib.pyplot as plt

f = open("./input.txt")
lines = f.readlines()

l = [x.strip().split(":") for x in lines]

a_l = {}

for i in l : 
    a_l[i[0]] = i[1].strip().split(' ')

nodes = []


connections = []
for k in a_l : 
    for j in a_l[k] :
        if (k, j) not in connections :
            if k not in nodes :
                nodes.append(k)
            if j not in nodes :
                nodes.append(j)
            connections.append((k,j))

m = {}

for i, v in connections :
    if i not in m : 
        m[i] = [v]
    else : 
        if v not in m[i] :
            m[i].append(v)

    if v not in m :
        m[v] = [i]
    else :
        if i not in m[v] :
            m[v].append(i)


def dfs(start, m):
    stack = [start]
    seen = set()

    while len(stack) > 0 :
        i = stack.pop(0)
        seen.add(i)

        if i not in m :
            continue

        for n in m[i] :

            if n not in seen:
                stack.append(n)

    return len(seen)

# Find connecting nodes using a graph visualizer tool
# G = nx.Graph() 
# G.add_edges_from(connections) 
# nx.draw_networkx(G) 
# plt.show() 

# Nodes
# (vps, pzc)
# (dph, cvx)
# (xvk, sgc)
removal_nodes = [("vps", "pzc"), ("dph", "cvx"), ("xvk", "sgc")]

for f, t in removal_nodes :
    t_i = m[f].index(t)
    m[f].pop(t_i)
    f_i = m[t].index(f)
    m[t].pop(f_i)

p1 = dfs(list(m.keys())[0], m)
p2 = len(nodes) - p1

part_one = p1* p2

print(part_one)


    

