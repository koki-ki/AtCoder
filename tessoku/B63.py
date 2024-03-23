from collections import deque

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

sy -= 1
sx -= 1
gy -= 1
gx -= 1

S = [input() for _ in range(r)]

dist = [[-1 for _ in range(c)] for _ in range(r)]
dist[sy][sx] = 0

Q = deque([])
Q.append((sy, sx))

dydx = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while Q:
    y, x = Q.popleft()
    for dy, dx in dydx:
        y2, x2 = y + dy, x + dx
        if not (0 <= x2 < c and 0 <= y2 < r):
            continue

        if S[y2][x2] == "#":
            continue

        if dist[y2][x2] == -1:
            dist[y2][x2] = dist[y][x] + 1
            Q.append((y2, x2))

print(dist[gy][gx])
