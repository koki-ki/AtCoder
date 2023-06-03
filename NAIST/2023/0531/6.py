from collections import defaultdict, deque

n = int(input())
G = defaultdict(list)

for _ in range(n):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

reachables = {1}
togo = deque()
togo.append(1)

while togo:
    f = togo.popleft()
    for nf in G[f]:
        if nf in reachables:
            continue
        else:
            togo.append(nf)
            reachables.add(nf)

ans = max(reachables)
print(ans)
