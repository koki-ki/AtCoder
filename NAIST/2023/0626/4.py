n, w = map(int, input().split())
used_water = [0 for _ in range(2 * 10**5 + 1)]
imos = [0 for _ in range(2 * 10 ** 5 + 1)]

for _ in range(n):
    s, t, p = map(int, input().split())
    imos[s] += p
    imos[t] -= p

for i in range(2 * 10**5 + 1):
    used_water[i] = used_water[i - 1] + imos[i]

if max(used_water) > w:
    print('No')
else:
    print('Yes')

