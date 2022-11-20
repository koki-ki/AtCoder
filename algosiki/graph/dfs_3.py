n, m = map(int, input().split())
G = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)

for g in G:
    g.sort()
visited = [False for _ in range(n + 1)]
q = []


def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for next_v in G[v]:
        if visited[next_v]:
            continue
        dfs(next_v)


dfs(0)
