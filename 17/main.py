from functools import cmp_to_key
from queue import PriorityQueue
import math

f = open("./input.txt")
grid = [x.strip() for x in f.readlines()]

def get_current_direction(prev_x, prev_y, curr_x, curr_y) :
    if prev_x == curr_x : 
        if curr_y > prev_y :
            return "s"
        if curr_y < prev_y : 
            return "n"

    if prev_y == curr_y :
        if curr_x > prev_x :
            return "e"
        if curr_x < prev_x : 
            return "w"


def get_nodes(node, nodes) :
    offsets = [ (1, 0), (-1,0) ,(0, 1), (0, -1)]

    x,y,streak,direction = node
    new_nodes = []
    
    for offset in offsets :
        offset_x, offset_y = offset
        new_x = x + offset_x
        new_y = y + offset_y
        if new_x < 0 or new_x >= len(nodes[y]) or new_y < 0 or new_y >= len(nodes):
            continue
        next_node = (x + offset_x , y + offset_y)
        new_direction = get_current_direction(x, y, new_x, new_y)
        if direction == "e" and new_direction == "w" or direction == "w" and new_direction == "e" or direction == "n" and new_direction == "s" or direction == "s" and new_direction == "n" :
            continue
        new_streak = streak + 1 if direction == new_direction else 1
        new_node = (x + offset_x, y+ offset_y, new_streak, new_direction)
        new_nodes.append(new_node)

    return new_nodes



def dijkstras(nodes):
    # (x, y, streak, direction) , value
    pqueue = PriorityQueue()
    pqueue.put((0 , (0,0,0, "e")))
    visited = {}
    prev = {}
    distances = {}
    distances[(0, 0, 0, "e")] = 0
    acc = []

    while not pqueue.empty() :
        value, current_node = pqueue.get(0)
        x, y, streak, direction = current_node

        if x == len(nodes[y]) - 1 and y == len(nodes) - 1 :
            acc.append(current_node)

        if current_node in visited:
            continue

        visited[current_node] = True

        new_nodes = get_nodes(current_node, nodes)
        

        for node in new_nodes :
            next_x, next_y, new_streak, new_direction = node
            next_distance = distances[current_node] + int(nodes[next_y][next_x])

            if node in visited : 
                continue

            if new_streak > 10 :
                continue
            if streak < 4 and direction != new_direction :
                continue

            if new_streak < 4 and len(nodes[next_y]) - 1 == next_x and len(nodes) - 1 == next_y :
                continue



            if node not in distances or next_distance < distances[node] :
                distances[node] = next_distance
                prev[node] = current_node
                pqueue.put((next_distance, node))

    return distances, prev, acc


dists, prev, acc = dijkstras(grid)

def get_min_key(distances, acc) :
    v = float("inf")
    k = None
    for i in acc :
        if distances[i] < v :
            v = distances[i]
            k = i
    return k, v

last_node, v = get_min_key(dists, acc)
print(v)

def find_path(nodes, node) :
    node = nodes[node]
    path = []

    while node in nodes :
        path.append(node)
        node = nodes[node]

    return list(reversed(path))
        
        
        
path = find_path(prev, last_node)

#
def print_grid(grid) :
    print("\n".join(["".join(x) for x in grid]))
print_grid(grid)
print("-------")
for i in path :
    x,y, _, _  = i
    list_grid = list(grid[y])
    list_grid[x] = "#"
    grid[y] = "".join(list_grid)


print_grid(grid)

