import sys
sys.setrecursionlimit(10 ** 8)


def dfs(v, G, seen, prev):
    seen[v] = True
    for v2 in G[v]:
        if seen[v2]:
            continue

        prev[v2] = v
        dfs(v2, G, seen, prev)


n, m = map(int, input().split())
G = [[] for _ in range(n + 1)]


for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

seen = [False for _ in range(n + 1)]
prev = [-1 for _ in range(n + 1)]

dfs(1, G, seen, prev)
order = []

now = n
while now != -1:
    order.append(now)
    now = prev[now]

order.reverse()
print(*order)
