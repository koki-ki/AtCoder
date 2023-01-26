def dfs(v):
    global ans, visited
    if ans == 10 ** 6:
        return
    ans += 1
    visited[v] = True
    for next_v in G[v]:
        if visited[next_v]:
            continue
        dfs(next_v)
    visited[v] = False


# main
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

ans = 0
visited = [False] * n

dfs(0)
print(ans)
