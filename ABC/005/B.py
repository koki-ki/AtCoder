n = int(input())
INF = 10 ** 18
ans = INF
for _ in range(n):
    t = int(input())
    ans = min(ans, t)
print(ans)