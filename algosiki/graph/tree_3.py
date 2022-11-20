import sys
sys.setrecursionlimit(10 ** 8)
n = int(input())
G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

dist = [-1 for _ in range(n)]
visited = [False for _ in range(n)]
dist[0] = 0


def dfs(v):
    visited[v] = True
    for nv in G[v]:
        if visited[nv]:
            continue
        dist[nv] = dist[v] + 1
        dfs(nv)


dfs(0)
ans = max(dist)
print(ans)
