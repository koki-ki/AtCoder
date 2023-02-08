from collections import Counter
n = int(input())
s = []

for si in range(n):
    s.append(input())

digits = list('0123456789')
ans = 1 << 60

for d in digits:
    pos = []
    for si in s:
        for i, sii in enumerate(si):
            if sii == d:
                pos.append(i)
    pos.sort()
    pos = Counter(pos)
    tmps = []
    for pk in pos.keys():
        tmps.append(pk + (pos[pk] - 1) * 10)
    ans = min(ans, max(tmps))
print(ans)
