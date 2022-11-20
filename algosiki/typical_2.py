import sys
sys.setrecursionlimit(10 ** 8)

n, m, s, t = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)

visited = [False for _ in range(n)]
prev = [-1 for _ in range(n)]


def dfs(v, G, visited, prev):
    visited[v] = True
    for nv in G[v]:
        if visited[nv]:
            continue
        prev[nv] = v
        dfs(nv, G, visited, prev)


dfs(s, G, visited, prev)

path = []
v = t
while v != s:
    path.append(v)
    v = prev[v]
path.append(v)
path.reverse()
print(len(path))
print(*path)
