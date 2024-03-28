n = int(input())
w = [0 for _ in range(n)]
x = [0 for _ in range(n)]

for i in range(n):
    w[i], x[i] = map(int, input().split())

ans = 0

for t in range(24):
    tmp = 0
    for i in range(n):
        if 9 <= (t + x[i]) % 24 <= 17:
            tmp += w[i]

    ans = max(ans, tmp)

print(ans)
