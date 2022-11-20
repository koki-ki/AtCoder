n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)

for i in range(n):
    G[i].sort()
visited = [False for _ in range(n)]
order = []


def rec(v):
    visited[v] = True
    for nv in G[v]:
        if visited[nv]:
            continue
        rec(nv)
    order.append(v)


for v in range(n):
    if visited[v]:
        continue
    rec(v)
order.reverse()
print(*order)
