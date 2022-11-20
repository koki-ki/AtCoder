n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)

visited = [False for _ in range(n)]
ans = n


def dfs(v):
    global ans
    visited[v] = True
    ans -= 1
    for nv in G[v]:
        if visited[nv]:
            continue
        dfs(nv)


dfs(0)
print(ans)
