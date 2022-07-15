n, k = map(int, input().split())
ans = 0

for i in range(n):
    for j in range(k):
        ans += 100 * (i + 1) + (j + 1)

print(ans)
