from collections import deque
n = int(input())
G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

dist = [-1 for _ in range(n)]
visited = [False for _ in range(n)]
dist[0] = 0

que = deque([])
que.append(0)

while len(que) > 0:
    v = que.popleft()
    for nv in G[v]:
        if dist[nv] != -1:
            continue
        dist[nv] = dist[v] + 1
        que.append(nv)

ans = max(dist)
print(ans)
