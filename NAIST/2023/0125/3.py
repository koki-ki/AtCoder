from collections import Counter
n = int(input())
s = []

for si in range(n):
    s.append(input())

digits = list('0123456789')
ans = 1 << 60

for d in digits:
    pos = []
    #
    sec = [0] * n
    #
    for si in s:
        for i, sii in enumerate(si):
            if sii == d:
                pos.append(i)
    pos.sort()
    pos = Counter(pos)
    tmp = max(pos.keys())
    for p in pos:
        tmp += 10 * (pos[p] - 1)
    ans = min(tmp, ans)

print(ans)
