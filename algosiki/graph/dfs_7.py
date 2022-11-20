dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def isvalid(x, y, h, w):
    if 0 <= x < h and 0 <= y < w:
        return True
    else:
        return False


def getnum(x, y, h, w):
    return x * w + y


def dfs(v, G, seen):
    seen[v] = True
    for nv in G[v]:
        if seen[nv]:
            continue
        dfs(nv, G, seen)


h, w = map(int, input().split())
grid = [[0 for _ in range(w)] for _ in range(h)]

for x in range(h):
    s = input()
    for y in range(w):
        if s[y] == '#':
            grid[x][y] = 1
        else:
            grid[x][y] = 0

G = [[] for _ in range(h * w)]

for x in range(h):
    for y in range(w):
        if grid[x][y] == 0:
            continue
        v = getnum(x, y, h, w)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if isvalid(nx, ny, h, w):
                if grid[nx][ny] == 0:
                    continue

                nv = getnum(nx, ny, h, w)
                G[v].append(nv)

seen = [False for _ in range(h * w)]

ans = 0

for x in range(h):
    for y in range(w):
        if grid[x][y] == 0:
            continue

        v = getnum(x, y, h, w)
        if seen[v]:
            continue

        dfs(v, G, seen)
        ans += 1

print(ans)
