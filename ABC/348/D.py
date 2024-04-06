from collections import deque

h, w = map(int, input().split())
a = []
for _ in range(h):
    a.append(list(input()))

for x in range(h):
    for y in range(w):
        if a[x][y] == "S":
            sx, sy = x, y
        if a[x][y] == "T":
            gx, gy = x, y

n = int(input())
medicines = []
for i in range(n):
    r, c, e = map(int, input().split())
    r, c = r - 1, c - 1
    a[r][c] = e
    medicines.append((r, c))

if a[sx][sy] == "S":
    print("No")
    exit()

for x in range(h):
    for y in range(w):
        if a[x][y] == "T":
            gx, gy = x, y


dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for medicine in medicines:
    r, c = medicine
    q = deque([(r, c)])
    while q:
        x, y = q.popleft()
        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and a[nx][ny] != "#":
                if a[nx][ny] == "T":
                    a[nx][ny] = a[x][y] - 1
                elif a[nx][ny] == ".":
                    a[nx][ny] = a[x][y] - 1
                    if a[nx][ny] > 0:
                        q.append((nx, ny))
                elif a[nx][ny] != "." and a[nx][ny] < a[x][y] - 1:
                    a[nx][ny] = a[x][y] - 1
                    q.append((nx, ny))


q = deque([(sx, sy)])
reachable = set()
while q:
    x, y = q.popleft()
    for dx, dy in dxdy:
        nx, ny = x + dx, y + dy
        if (nx, ny) in reachable:
            continue
        if 0 <= nx < h and 0 <= ny < w and a[nx][ny] != "#" and a[nx][ny] >= 0:
            reachable.add((nx, ny))
            if a[nx][ny] > 0:
                q.append((nx, ny))

if (gx, gy) in reachable:
    print("Yes")
else:
    print("No")
