n = int(input())
s = []
for _ in range(5):
    s.append(input())
dp = [[0 for _ in range(5)] for _ in range(n + 10)]
for i in range(n):
    b_cnt = 0
    w_cnt = 0
    r_cnt = 0
    for j in range(5):
        if s[j][i] == "R":
            b_cnt += 1
            w_cnt += 1
        elif s[j][i] == "B":
            r_cnt += 1
            w_cnt += 1
        elif s[j][i] == "W":
            b_cnt += 1
            r_cnt += 1
        else:
            b_cnt += 1
            w_cnt += 1
            r_cnt += 1

    dp[i + 1][0] = min(dp[i][1], dp[i][2]) + b_cnt
    dp[i + 1][1] = min(dp[i][0], dp[i][2]) + w_cnt
    dp[i + 1][2] = min(dp[i][0], dp[i][1]) + r_cnt

print(min(dp[n][0], dp[n][1], dp[n][2]))