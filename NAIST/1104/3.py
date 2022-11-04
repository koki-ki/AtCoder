N, X = map(int, input().split())
a = []
b = []
for _ in range(N):
    a_, b_ = map(int, input().split())
    a.append(a_)
    b.append(b_)
dp = [[False] * (X + 1) for _ in range(N + 1)]
dp[0][0] = True
for i in range(N):
    for x in range(X):
        if dp[i][x] == True:
            if x + a[i] <= X:
                dp[i + 1][x + a[i]] = True
            if x + b[i] <= X:
                dp[i + 1][x + b[i]] = True
if dp[N][X] == True:
    print('Yes')
else:
    print('No')
