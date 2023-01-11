n, w = map(int, input().split())
s, t, p = [], [], []
for i in range(n):
    s_, t_, p_ = map(int, input().split())
    s.append(s_)
    t.append(t_)
    p.append(p_)

fueru = [(s[i], p[i]) for i in range(n)]
heru = [(t[i], p[i]) for i in range(n)]

fueru.sort(key = lambda x: x[0])
heru.sort(key = lambda x: x[0])

a = [0] * n
for i in range(n):
    for j in range()

