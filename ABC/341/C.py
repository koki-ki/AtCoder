h, w, n = map(int, input().split())
t = input()
dxdy = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

s = [input() for _ in range(h)]
ans = 0
for x in range(1, h - 1):
    for y in range(1, w - 1):
        if s[x][y] == "#":
            continue
        start = (x, y)
        nx, ny = start
        flag = True
        for ti in t:
            dx, dy = dxdy[ti]
            nx, ny = nx + dx, ny + dy
            if nx < 0 or nx >= h or ny < 0 or ny >= w or s[nx][ny] == "#":
                flag = False
                break
        if flag:
            ans += 1

print(ans)
