INF = 1 << 60

n, a, b = map(int, input().split())
s = input() * 2

ans = INF

for i in range(n):
    tmp = a * i
    for j in range(n // 2):
        if s[i + j] != s[i + n - 1 - j]:
            tmp += b

    ans = min(ans, tmp)

print(ans)
