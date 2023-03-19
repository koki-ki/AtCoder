MOD = 10 ** 9 + 7
n = int(input())
a = list(map(int, input().split()))

accu = [0 for _ in range(n)]
accu[0] = a[0]
for i in range(1, n):
    accu[i] = accu[i - 1] + a[i]
ans = 0
for i in range(n):
    ans += a[i] * (accu[n - 1] - accu[i]) % MOD
print(ans % MOD)