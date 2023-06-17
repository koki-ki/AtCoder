def dfs(pos, cur):
    col[pos] = cur
    for i in G[pos]:
        if col[i] >= 1:
            continue
        dfs(i, 3 - cur)


n = int(input())
G = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    ai, bi = map(int, input().split())
    G[ai].append(bi)
    G[bi].append(ai)

col = [0 for _ in range(n + 1)]

dfs(1, 1)

g1 = []
g2 = []

for i in range(1, n + 1):
    if col[i] == 1:
        g1.append(i)
    else:
        g2.append(i)

ans = []

if len(g1) > len(g2):
    for i in range(0, n//2):
        ans.append(g1[i])
else:
    for i in range(n // 2):
        ans.append(g2[i])

print(*ans)
