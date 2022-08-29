n, x = map(int, input().split())
a = [0]
b = [0]
for i in range(n):
    a_, b_ = map(int, input().split())
    a.append(a_)
    b.append(b_)

# dp[i][j]: i回ジャンプした後に地点jにいることは可能か
dp = [[0] * (10 ** 4 + 1) for _ in range(n + 2)]
dp[1][a[1]] = 1
dp[1][b[1]] = 1
for i in range(1, n + 1):
    for j in range(x):
        if dp[i][j] == 1:
            dp[i + 1][j + a[i]] = 1
            dp[i + 1][j + b[i]] = 1

if dp[n + 1][x] == 1:
    print('Yes')
else:
    print('No')
