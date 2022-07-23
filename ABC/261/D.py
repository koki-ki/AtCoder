n, m = map(int, input().split())
x = list(map(int, input().split()))
c = []
y = []

for i in range(m):
    c_, y_ = map(int, input().split())
    c.append(c_)
    y.append(y_)

# dp = [[0] * 2 for _ in range(m)]
# dp[0][0] = x[0]
dp = [0] * n
dp[0] = x[0]

for i in range(m):
    if c[i] == 1:
        # dp[0][0] += y[0]
        dp[0] += y[i]

cnt = 1

for i in range(1, n):
    omote = dp[i - 1] + x[i]
    ura = dp[i - 1]
    for j in range(m):
        if cnt + 1 == c[j]:
            tmpv = max(tmpv, dp[i] + y[j])
    if tmpv == dp[i]:
        cnt += 1
    else:
        cnt = 1

print(dp[n - 1])

