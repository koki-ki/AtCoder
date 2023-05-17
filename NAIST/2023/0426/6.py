n, m = map(int, input().split())
k = []
s = []
for _ in range(m):
    ki, *si = list(map(int, input().split()))
    k.append(ki)
    s.append(si)
p = list(map(int, input().split()))

ans = 0

for i in range(2 ** 10):
    switches = [False for _ in range(n + 1)]
    lumps = [False for _ in range(m + 1)]
    for j in range(m):
        switches[j] = True if i >> j % 2 == 0 else False

    for i, pi, si in enumerate(p, s):
        cnt = 0
        for ssi in si:
            cnt += switches[ssi]
        if cnt % 2 == pi:
            lumps[i] = True

    if lumps[1:].count(True) == m:
        ans += 1

print(ans)