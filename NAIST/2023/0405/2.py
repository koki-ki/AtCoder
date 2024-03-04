x = int(input())
items = [item for item in range(100, 106)]

dp = [False for _ in range(10 ** 5 + 1)]

for i in range(100, 106):
    dp[i] = True

for i in range(100, 10 ** 5 + 1):
    for item in items:
        if item + i <= 10 ** 5 and dp[i]:
            dp[item + i] = True

if dp[x]:
    print(1)
else:
    print(0)
