from collections import deque
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

color = [-1 for _ in range(n)]
ans = 'Yes'
for v in range(n):
    if color[v] != -1:
        continue
    deq = deque([])
    color[v] = 0
    deq.append(v)
    while len(deq) > 0:
        qv = deq.popleft()
        for nv in G[qv]:
            if color[nv] != -1:
                if color[nv] == color[qv]:
                    ans = 'No'
                continue

            color[nv] = 1 - color[qv]
            deq.append(nv)

print(ans)
