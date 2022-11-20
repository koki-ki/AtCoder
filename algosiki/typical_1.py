import sys
sys.setrecursionlimit(100000)

n, m, s, t = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)

visited = [False for _ in range(n)]


def dfs(v):
    visited[v] = True
    for nv in G[v]:
        if visited[nv]:
            continue
        dfs(nv)


dfs(s)
if visited[t]:
    print('Yes')
else:
    print('No')
