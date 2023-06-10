from bisect import bisect_left as bl

n = int(input())
a = list(map(int, input().split()))
q = int(input())
l, r = [], []
for _ in range(q):
    li, ri = map(int, input().split())
    l.append(li)
    r.append(ri)

divided = [0] + [a[i] - a[i - 1] for i in range(1, n + 1)][1:]

accumulates = [0 for _ in range(n + 1)]

for i in range(n):
    if i % 2 == 1:
        accumulates[i + 1] = accumulates[i] + divided[i]
    else:
        accumulates[i + 1] = accumulates[i]

print(*divided)
print(*accumulates)
print(len(divided), len(accumulates)

for li, ri in zip(l, r):
    idl = bl(a, li)
    idr = bl(a, ri)
    ans = divided[idl] - li + ri - divided[idr]
    ans += accumulates[idr] - accumulates[idl]
    print(ans)

