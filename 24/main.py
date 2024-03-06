from math import floor

f = open("./input.txt")
lines = [x.strip() for x in f.readlines()]

mn = 200000000000000
mx = 400000000000000


s = [[[int(z) for z in y.split(",")] for y in x.split("@")] for x in lines]

def line_intersection(line1, line2):
    x1, x2, x3, x4 = line1[0][0], line1[1][0], line2[0][0], line2[1][0]
    y1, y2, y3, y4 = line1[0][1], line1[1][1], line2[0][1], line2[1][1]

    dx1 = x2 - x1
    dx2 = x4 - x3
    dy1 = y2 - y1
    dy2 = y4 - y3
    dx3 = x1 - x3
    dy3 = y1 - y3

    det = dx1 * dy2 - dx2 * dy1
    det1 = dx1 * dy3 - dx3 * dy1
    det2 = dx2 * dy3 - dx3 * dy2

    if det == 0.0:  # lines are parallel
        if det1 != 0.0 or det2 != 0.0:  # lines are not co-linear
            return None  # so no solution

        if dx1:
            if x1 < x3 < x2 or x1 > x3 > x2:
                return math.inf  # infinitely many solutions
        else:
            if y1 < y3 < y2 or y1 > y3 > y2:
                return math.inf  # infinitely many solutions
        return None  # no intersection

    s = det1 / det
    t = det2 / det

    if 0.0 < s < 1.0 and 0.0 < t < 1.0:
        return x1 + t * dx1, y1 + t * dy1

def calc_segment_end(x,y,vx, vy) :
    if vx < 0  and vy < 0:
        offset = min((mn - x) / vx, (mn - y) / vy)

    if vx < 0 and vy > 0  :
        offset = min((mn - x) / vx, (mx - y) / vy)

    if vx > 0 and vy < 0 :
        offset =  min((mx - x) / vx, (mn - y)  / vy)

    if vx >0 and vy > 0 :
        offset = min((mx - x) / vx , (mx - y) / vy)


    return (x + offset * vx, y + offset * vy)


part_one = 0

for i, line in enumerate(s) :
    l ,v = line
    lx, ly, _ = l
    vx , vy, _ = v

    el = calc_segment_end(lx, ly, vx, vy)

    for j in range(i, len(s)) :
        dl, dv = s[j]
        dlx, dly, _ = dl
        dvx, dvy, _ = dv

        edl = calc_segment_end(dlx, dly, dvx, dvy)

        k = line_intersection((l, el), (dl, edl))

        if k :
            if mn <= k[0] <= mx and mn <= k[1] <= mx :
                part_one += 1



import sympy
print(part_one)

hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in open("./input.txt")]

xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")


equations = []

for sx, sy, sz, vx, vy, vz in hailstones :
    equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
    equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))

answer = sympy.solve(equations)[0]

part_two = int(answer[xr]) + int(answer[yr]) + int(answer[zr])

print(part_two)
