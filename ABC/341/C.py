h, w, n = map(int, input().split())
t = input()
s = [input() for _ in range(h)]

cands = set()

dxdy = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

for x in range(1, h - 1):
    for y in range(1, w - 1):
        flag = True
        if s[x][y] == '#':
            continue
        for ti in t:
            dx, dy = dxdy[ti]
            x = x + dx
            y = y + dy

            if not (0 <= x <= h - 1 and 0 <= y <= w - 1) or s[x][y] == '#':
                flag = False
                break
        if flag:
            cands.add((x, y))

ans = len(cands)
print(ans)
