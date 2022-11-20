n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

visited = [False for _ in range(n)]


def dfs(v):
    visited[v] = True
    for nv in G[v]:
        if visited[nv]:
            continue
        dfs(nv)


dfs(0)
if False in visited:
    print('No')
else:
    print('Yes')
