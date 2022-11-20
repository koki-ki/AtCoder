from collections import defaultdict, deque
n = int(input())
G = defaultdict(list)
for _ in range(n):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

que = deque()
que.append(1)

S = {1}
while que:
    v = que.popleft()
    for i in G[v]:
        if i not in S:
            que.append(i)
            S.add(i)
print(max(S))
