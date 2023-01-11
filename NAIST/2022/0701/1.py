v, t, s, d = map(int, input().split())
vt = v * t
vs = v * s
if not(vt <= d and d <= vs):
    print('Yes')
else:
    print('No')