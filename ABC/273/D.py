h, w, rs, cs = map(int, input().split())
n = int(input())
r = []
c = []
for _ in range(n):
    r_, c_ = map(int, input().split())
    r.append(r_)
    c.append(c_)
q = int(input())
d = []
l = []
for _ in range(q):
    d_, l_ = map(int, input().split())
    d.append(d_)
    l.append(l_)
