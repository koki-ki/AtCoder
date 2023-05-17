from math import factorial

MOD = 998244353
n, m, k = map(int, input().split())

ans = factorial(k - 1) // (factorial(k - n) * factorial(n - 1)) % MOD

print(ans)