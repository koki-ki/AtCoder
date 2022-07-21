from collections import deque
h, w = map(int, input().split())

c = []
for i in range(h):
    c.append(input())

sh, sw = 0, 0
gh, gw = 0, 0

# スタート、ゴールの位置
for i in range(h):
    for j in range(w):
        if c[i][j] == 's':
            sh, sw = i, j
        if c[i][j] == 'g':
            gh, gw = i, j

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

INF = int(1e9)
D = [[INF] * w for _ in range(h)]

def dfs():
    que = deque()
    que.append([sh, sw])
    D[sh][sw] = 0

    while que:
        p = que.pop()
        if p[0] == gh and p[1] == gw:
            break
        for i in range(4):
            nh = p[0] + dx[i]
            nw = p[1] + dy[i]

            if 0 <= nh < h and 0 <= nw < w and c[nh][nw] != '#' and D[nh][nw] == INF:
                que.append([nh, nw])
                D[nh][nw] = D[p[0]][p[1]] + 1

    return D[gh][gw]

ans = dfs()
if ans != INF:
    print('Yes')
else:
    print('No')
