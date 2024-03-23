import heapq

INF = 10 ** 10

n, m = map(int, input().split())
G = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))

kakutei = [False for _ in range(n + 1)]
cur = [INF for _ in range(n + 1)]
cur[1] = 0
Q = []
heapq.heappush(Q, (cur[1], 1))  # (暫定距離, ノード番号)

while len(Q) >= 1:
    pos = heapq.heappop(Q)[1]

    if kakutei[pos]:
        continue

    kakutei[pos] = True
    for e in G[pos]:
        if cur[e[0]] > cur[pos] + e[1]:
            cur[e[0]] = cur[pos] + e[1]
            heapq.heappush(Q, (cur[e[0]], e[0]))

for i in range(1, n + 1):
    if cur[i] != INF:
        print(cur[i])
    else:
        print(-1)
