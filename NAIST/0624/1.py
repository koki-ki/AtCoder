n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += i * 10000
ans //= n
print(ans)