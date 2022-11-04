from itertools import combinations, permutations
from math import sqrt

s = []
for _ in range(9):
    s.append(input())
p = []
for i in range(9):
    for j in range(9):
        if s[i][j] == '#':
            p.append((i, j))

sets = combinations(p, 4)
ans = 0


def inp(v1, v2):
    return v1[0] * v2[0] + v1[1] + v2[1]


def ort(v1, v2):
    if inp(v1, v2) == 0:
        return True
    else:
        return False


def norm(v):
    return sqrt(v[0] ** 2 + v[1] ** 2)


for s in sets:
    p1, p2, p3, p4 = s
    x1 = p1[0]
    x2 = p2[0]
    x3 = p3[0]
    x4 = p4[0]
    y1 = p1[1]
    y2 = p2[1]
    y3 = p3[1]
    y4 = p4[1]

    g = ((x1 + x2 + x3 + x4) / 4, (y1 + y2 + y3 + y4) / 4)

    # /v1 = (x1 - x2, y1 - y2)
    # v2 = (x3 - x4, y3 - y4)
    v1 = (x1 - g[0], y1 - g[1])
    v2 = (x2 - g[0], y2 - g[1])
    v3 = (x3 - g[0], y3 - g[1])
    v4 = (x4 - g[0], y4 - g[1])
    if norm(v1) == norm(v2) == norm(v3) == norm(v4):
        sets2 = permutations([v1, v2, v3, v4])
        for s2 in sets2:
            V1, V2, V3, V4 = s2
            if ort(V1, V2) and ort(V3, V4):
                ans += 1


print(ans)
