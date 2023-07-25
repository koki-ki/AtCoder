def dfs(v, G, used):
    

n1, n2, m = map(int, input().split())
G = [[] for _ in range(n1 + n2 + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

    