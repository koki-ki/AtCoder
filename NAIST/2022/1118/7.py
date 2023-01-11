n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))
