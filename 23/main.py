f = open("./input.txt")
grid= [x.strip() for x in f.readlines()]

start = (grid[0].index("."),0)
end = (grid[len(grid) - 1].index("."),  len(grid) - 1)

slope_map = {
    "v" : (0, 1),
    "^" : (0, -1),
    ">" : (1, 0), 
    "<" : (-1, 0)
}

offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# cursor, prev, length, is_complete
paths = [(start,(0, 0),0)]
path_lengths = []

while len(paths) > 0 :
    p = paths.pop(0)
    cursor, prev, length = p 
    x, y = cursor

    if cursor == end :
        path_lengths.append(length)
        continue

    if grid[y][x] in slope_map :
        o_x, o_y = slope_map[grid[y][x]]
        n_c = (x + o_x, y + o_y)

        paths.append((n_c, cursor, length + 1))
        continue


    for o in offsets :
        o_x, o_y = o
        x, y = cursor

        n = (x + o_x, y + o_y)
        n_x , n_y = n

        if n_x < 0 or n_x >= len(grid[y]) or n_y < 0 or n_y > len(grid) :
            continue

        if n == prev :
            continue

        if grid[n_y][n_x] != "#" :
            if grid[n_y][n_x] == "v" and o == (0, -1) :
                continue
            if grid[n_y][n_x] == "<" and o == (1, 0) :
                continue
            if grid[n_y][n_x] == "^" and o == (0, 1) :
                continue

            if grid[n_y][n_x] == ">" and o == (-1, 0) :
                continue
            paths.append((n, cursor, length + 1))

part_one = max(path_lengths)
print(part_one)


ps = [start, end]

for y, row in enumerate(grid):
    for x, ch in enumerate(row):
        if ch == "#" :
            continue
        neighbors = 0
        for nx, ny in [(x - 1, y), (x+ 1, y), (x, y + 1), (x, y - 1)] :
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] != "#" :
                neighbors += 1

        if neighbors >= 3 :
            ps.append((x, y))

graph = {pt :{} for pt in ps}
    
for sx, sy in ps :
    stack = [(0 , sx, sy)]
    seen = {(sx, sy)}

    while stack :
        l,x,y = stack.pop(0)
        
        if l != 0 and (x, y) in ps :
            graph[(sx, sy)][(x, y)] = l
            continue

        for dx, dy in offsets :
            nx = x + dx
            ny = y + dy 
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] != "#" and (nx, ny) not in seen :
                stack.append((l + 1, nx ,ny))
                seen.add((nx, ny))

seen = set()
def dfs(pt):
    if pt == end :
        return 0
    m = -float("inf")
    
    seen.add(pt)
    for nx in graph[pt] : 
        if nx not in seen :
            m = max(m, dfs(nx) + graph[pt][nx])
    seen.remove(pt)

    return m

print(dfs(start))
# Not my solution, but I found the edge contraction part very interesting and it runs super fast when compared to the brute force.






