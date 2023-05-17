n = int(input())
G = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for g in G:
    g.sort()
    print(g)

visited = [False for _ in range(n + 1)]
num_visited = 0
cur = 1
pre = 1
ways = []
ways.append(cur)


