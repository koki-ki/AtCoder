n, m, x = map(int, input().split())
a = list(map(int, input().split()))
cost = [0 for _ in range(n + 1)]
for num in a:
    cost[num] = 1

for i in range(x - 1, -1, -1):
    cost[i] += cost[i + 1]

for i in range(x + 1, n + 1):
    cost[i] += cost[i - 1]

ans = min(cost[0], cost[n])
print(ans)