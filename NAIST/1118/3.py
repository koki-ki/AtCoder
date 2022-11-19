n = int(input())
imos = [0] * (2 + 10 ** 6)
for _ in range(n):
    a, b = map(int, input().split())
    imos[a] += 1
    imos[b + 1] -= 1
acc = [0] * (1 + 10 ** 6)
ans = 0
for i in range(1, 10 ** 6 + 1):
    acc[i] = acc[i - 1] + imos[i]
    ans += acc[i] * i
print(ans)
