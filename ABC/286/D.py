n, x = map(int, input().split())
a = [0]
b = [0]
for _ in range(n):
    a_, b_ = map(int, input().split())
    a.append(a_)
    b.append(b_)

dp = [[False for _ in range(x + 1)] for _ in range(n + 1)]
dp[0][0] = True

for i in range(1, n + 1):
    for j in range(x + 1):
        if dp[i - 1][j]:
            for k in range(b[i] + 1):
                if j + a[i] * k > x:
                    break
                else:
                    dp[i][j + a[i] * k] = True

if dp[n][x]:
    print('Yes')
else:
    print('No')

# for d in dp:
#     print(*d)
