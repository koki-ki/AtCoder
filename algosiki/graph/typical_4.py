import sys
sys.setrecursionlimit(10 ** 6)


def dfs(v, G, color):
    for nv in G[v]:
        if color[nv] != -1:
            if color[nv] == color[v]:
                return False
            continue

        color[nv] = 1 - color[v]

        if not dfs(nv, G, color):
            return False

    return True


n, m = map(int, input().split())
G = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)


color = [-1 for _ in range(n)]
ans = 'Yes'

for v in range(n):
    if color[v] != -1:
        continue

    color[v] = 1
    if not dfs(v, G, color):
        ans = 'No'

print(ans)
