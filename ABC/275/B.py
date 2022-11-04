a, b, c, d, e, f = map(int, input().split())

MOD = 998244353
ans = ((a * b * c) - (d * e * f)) % MOD
print(ans)
