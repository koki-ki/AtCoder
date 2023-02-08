MOD = 2019
l, r = map(int, input().split())

len_of_mods = min(r - l + 1, MOD)
mods = [0 for _ in range(len_of_mods)]

for i in range(len_of_mods):
    mods[i] = (l + i) % MOD

ans = MOD

for i in range(len_of_mods - 1):
    for j in range(i + 1, len_of_mods):
        ans = min(ans, mods[i] * mods[j] % MOD)
print(ans)