n, q = map(int, input().split())
l = []
a = []
for _ in range(n):
    ins = list(map(int, input().split()))
    l.append(ins[0])
    a.append(ins[1:])
s = []
t = []
for _ in range(q):
    s_, t_ = map(int, input().split())
    s.append(s_)
    t.append(t_)

for k in range(q):
    print(a[s[k] - 1][t[k] - 1])
