def dfs(v, G, seen):
    seen[v] = True

    for v2 in G[v]:
        if seen[v2]:
            continue
        dfs(v2, G, seen)


# main
n, m = map(int, input().split())
G = [[0] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

seen = [False for _ in range(n)]
ans = 0

for v in range(n):
    if seen[v]:
        continue
    dfs(v, G, seen)
    ans += 1


print(ans)
