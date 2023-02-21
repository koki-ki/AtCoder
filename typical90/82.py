MOD = 10 ** 9 + 7
def tousawa(i, l):
    return (i + l) * (l - i + 1) // 2

l, r = map(int, input().split())
kl = len(str(l))
kr = len(str(r))

ans = 0
ans += kl * tousawa(l, 10 ** kl - 1) % MOD
ans += sum([k * tousawa(10 ** (k - 1), 10 ** k - 1) % MOD for k in range(kl + 1, kr)])
ans += kr * tousawa(10 ** (kr - 1), r) % MOD
ans %= MOD
print(ans)