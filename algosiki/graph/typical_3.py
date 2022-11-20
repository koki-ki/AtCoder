from collections import deque

n, m, s, t = map(int, input().split())
G = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)

visited = [False for _ in range(n)]
prev = [-1 for _ in range(n)]


def bfs(s, G, visited, prev):
    deq = deque()
    visited[s] = True
    deq.append(s)
    while len(deq) > 0:
        v = deq.popleft()
        for nv in G[v]:
            if visited[nv]:
                continue
            visited[nv] = True
            prev[nv] = v
            deq.append(nv)


bfs(s, G, visited, prev)
path = []

v = t
while v != -1:
    path.append(v)
    v = prev[v]

path.reverse()
print(len(path))
print(*path)
