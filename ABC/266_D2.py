n = int(input())
INF = 10**18
M = 10 ** 5 + 5
dp = [[-INF] * 5 for _ in range(M)]
dp[0][0] = 0
x = [0] * M
a = [0] * M

for i in range(n):
    t_, x_, a_ = map(int, input().split())
    x[t_] = x_
    a[t_] = a_

for i in range(M - 1):
    ni = i + 1
    for j in range(5):
        for nj in range(j - 1, j + 2):
            if nj < 0 or nj >= 5:
                continue
            dp[ni][nj] = max(dp[ni][nj], dp[i][j])
    dp[ni][x[ni]] += a[ni]

ans = - INF
for j in range(5):
    ans = max(ans, dp[M-1][j])
print(ans)
