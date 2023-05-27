import heapq
from collections import defaultdict

n, m, h, k = map(int, input().split())
s = list(input())
x = 0
y = 0
ways = []

for si in s:
    if si == 'R':
        x += 1
    elif si == 'L':
        x -= 1
    elif si == 'U':
        y += 1
    else:
        y -= 1
    ways.append((x, y))

num_heals = defaultdict(int)

for _ in range(m):
    x, y = map(int, input().split())
    num_heals[(x, y)] += 1

for i, way in enumerate(ways, 1):
    h -= 1
    if h < 0 and i != n - 1:
        print('No')
        exit()

    if num_heals[way] >= 1 and h < k:
        h = k
        num_heals[way] -= 1

print('Yes')


