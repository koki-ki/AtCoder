from collections import defaultdict
h, w = map(int, input().split())
s = []
for _ in range(h):
    s.append(list(input()))
t = []
for _ in range(h):
    t.append(list(input()))


st = [''.join(x) for x in zip(*s)]
tt = [''.join(x) for x in zip(*t)]

sd = defaultdict(int)
td = defaultdict(int)

for i in range(w):
    sd[st[i]] += 1
    td[tt[i]] += 1


sd = sorted(sd.items())
td = sorted(td.items())

if sd == td:
    print('Yes')
else:
    print('No')
