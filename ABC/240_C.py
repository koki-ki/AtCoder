n, x = map(int, input().split())
a = [0]
b = [0]
for i in range(n):
    a_, b_ = map(int, input().split())
    a.append(a_)
    b.append(b_)

# dp[i][j]: i回ジャンプした後に地点jにいることは可能か
dp = [[0] * (10 ** 4 + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(10 ** 4 + 1):
        if dp[i][j] == 1:
            dp[i + 1][j + a[i + 1]] = 1
            dp[i + 1][j + b[i + 1]] = 1

if dp[n][x] == 1: print('Yes')
else: print('No')
