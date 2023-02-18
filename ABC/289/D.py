n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
x = int(input())

mochi = [False for _ in range(10 ** 5 + 1)]

for i in b:
    mochi[i] = True

stop = [False for _ in range(10 ** 5 + 1)]
dp = [False for _ in range(10 ** 5 + 1)]
dp[0] = True

for i in range(10 ** 5 + 1):
    if dp[i]:
        for step in a:
            if i + step > 10 ** 5:
                break
            if mochi[i + step]:
                stop[i + step] = True
            else:
                dp[i + step] = True

if stop[x] or dp[x]:
    print("Yes")
else:
    print("No")

