from collections import deque
h, w = map(int, input().split())
a = []
dist = [[-1 for _ in range(w)] for _ in range(h)]
dist[0][0] = 0
for _ in range(h):
    a.append(input())
dx = [0, 1]
dy = [1, 0]
Q = deque()
Q.append([0, 0])

while len(Q) > 0:
    curx, cury = Q.popleft()
    for x, y in zip(dx, dy):
        nextx = curx + x
        nexty = cury + y
        if not(0 <= nextx < h and 0 <= nexty < w):
            continue

        if a[nextx][nexty] == ".":
            continue

        dist[nextx][nexty] = dist[curx][cury] + 1
        Q.append([nextx, nexty])

flag = True
for x in range(h):
    for y in range(w):
        if a[x][y] == '#' and dist[x][y] == -1:
            flag = False
for i in range(h - 1):
    for j in range(w - 1):
        if a[i + 1][j] == "#" and a[i + 1][j + 1] == "#" and a[i][j + 1] == "#":
            flag = False
        if a[i][j] == "#" and a[i + 1][j] == "#" and a[i][j + 1] == "#":
            flag = False


if flag and dist[h - 1][w - 1] != -1:
    print("Possible")
else:
    print("Impossible")




