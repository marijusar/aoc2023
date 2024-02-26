from functools import cmp_to_key
import math

f = open("./test.txt")
grid = [x.strip() for x in f.readlines()]

def sort_edges(a,b) :
    _,  distance_a, _, _ = a
    _, distance_b, _, _ = b

    return distance_a- distance_b

def get_current_direction(prev_node, curr_node) :
    prev_x, prev_y = prev_node
    curr_x, curr_y = curr_node

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
    offsets = [(0, 1), (0, -1), (1, 0) , (-1,0)]
    x,y = node
    new_nodes = []
    
    for offset in offsets :
        offset_x, offset_y = offset
        new_x = x + offset_x
        new_y = y + offset_y
        if new_x < 0 or new_x >= len(nodes[y]) or new_y < 0 or new_y >= len(nodes):
            continue
        next_node = (x + offset_x , y + offset_y)
        new_nodes.append(next_node)
    return new_nodes

def get_node_cache_key(node, nodes) :
    x, y = node
    cache_key = len(nodes) * y + x
    return cache_key

def get_node_from_cache_key(key, grid) :
    x = key % len(grid)
    y = math.floor(key / len(grid))

    return (x, y)
    

def dijkstras(nodes):
    # coordinatates , value, streak, direction
    pqueue = [((0,0), 0, 0, "e")]
    visited = [False] * len(nodes) * len(nodes[0])
    prev = [None] * len(nodes) * len(nodes[0])
    distances = [float('inf')] * len(nodes) * len(nodes[0])
    distances[0] = 0

    while len(pqueue) > 0 :
        current_node, value, streak, direction  = pqueue.pop()
        cache_key = get_node_cache_key(current_node, nodes)

        if visited[cache_key] == True :
            continue

        visited[cache_key] == True

        new_nodes = get_nodes(current_node, nodes)

        for node in new_nodes :
            next_x, next_y = node
            next_cache_key = get_node_cache_key(node, nodes)
            next_distance = distances[cache_key] + int(nodes[next_y][next_x])
            new_direction = get_current_direction(current_node, node)
            new_streak = streak + 1 if direction == new_direction else 1
            if new_streak == 4 :
                continue

            if visited[next_cache_key] == True :
                continue

            if next_distance < distances[next_cache_key] :
                distances[next_cache_key] = next_distance
                prev[next_cache_key] = cache_key
                pqueue.append((node, next_distance, new_streak, new_direction ))
                pqueue.sort(key=cmp_to_key(sort_edges))
            print(pqueue)

    return (distances, prev)

    #     current_node, value, streak, direction  = pqueue.pop()
    #     x, y = current_node
    #     if x == len(nodes[0]) -1 and y == len(nodes) - 1 :
    #         return (distances, prev)
    #     cache_key = get_node_cache_key(current_node, nodes)
    #     visited[cache_key] = True
    #     new_nodes = get_nodes(current_node, nodes)
    #     for next_node in new_nodes :
    #         next_cache_key = get_node_cache_key(next_node, nodes)
    #         if visited[next_cache_key] :
    #             continue
    #         next_distance = distances[cache_key] + int(nodes[next_node[1]][next_node[0]])
    #         if next_distance < distances[next_cache_key] : 
    #             new_direction = get_current_direction(current_node, next_node)
    #             new_streak = streak + 1 if direction == new_direction else 1
    #             # if new_streak >= 4 :
    #             #     continue
    #             distances[next_cache_key] = next_distance
    #             prev[next_cache_key] = cache_key
    #             pqueue.append((next_node, next_distance, new_streak, new_direction ))
    #             pqueue.sort(key=cmp_to_key(sort_edges))
    # return (distances, prev)


distances, prev_nodes = dijkstras(grid)
print(distances)
print(distances[len(distances) - 1])

def find_path(nodes) :
    curr_node_idx = nodes[len(nodes) - 1]
    path = []

    while curr_node_idx != None :
        path.append(curr_node_idx)
        curr_node_idx = nodes[curr_node_idx]

    return list(reversed(path))
        
        
        
path = find_path(prev_nodes)
print(path)

def print_grid(grid) :
    print("\n".join(["".join(x) for x in grid]))

# print(path)

for i in path :
    x,y  = get_node_from_cache_key(i, grid)
    list_grid = list(grid[y])
    list_grid[x] = "#"
    grid[y] = "".join(list_grid)


print_grid(grid)

