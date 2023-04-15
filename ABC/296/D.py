INF = 2 * 10 ** 18
n, m = map(int, input().split())
ans = INF
for i in range(1, n + 1):
    x = (m + i - 1) // i
    if x <= n:
        ans = min(ans, i * x)
    if i > x:
        break

if ans == INF:
    print(-1)
else:
    print(ans)
