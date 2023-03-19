from collections import deque 

n, q = map(int, input().split())
G = [[] for _ in range(n + 1)]
for _ in range(n):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

queries = []
for _ in range(q):
    c, d = map(int, input().split())
    queries.append((c, d))

dist = [10 ** 5 for _ in range(n + 1)]
dist[1] = 0 
to_visit = deque()
to_visit.append(1)
while len(to_visit):
    cur = to_visit.popleft()
    if dist[cur] != 10 ** 5:
        continue 
    
for query in queries:
    c, d = query
    if         
    