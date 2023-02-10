# input
n = int(input())
c = []
p = []
for _ in range(n):
    ci, pi = map(int, input().split())
    c.append(ci)
    p.append(pi)
q = int(input())
l = []
r = []
for _ in range(q):
    li, ri = map(int, input().split())
    li -= 1
    ri -= 1
    l.append(li)
    r.append(ri)
# main
acc1 = [0 for _ in range(n)]
acc2 = [0 for _ in range(n)]
acc1[0] = p[0] if c[0] == 1 else 0
acc2[0] = p[0] if c[0] == 2 else 0

for i in range(1, n):
    if c[i] == 1:
        acc1[i] += acc1[i - 1] + p[i]
        acc2[i] = acc2[i - 1]
    else:
        acc1[i] = acc1[i - 1]
        acc2[i] += acc2[i - 1] + p[i]

for li, ri in zip(l, r):
    a = acc1[ri] - acc1[li] + (p[li] if c[li] == 1 else 0)
    b = acc2[ri] - acc2[li] + (p[li] if c[li] == 2 else 0)
    print(a, b)

