l, n1, n2 = map(int, input().split())
v = [[] for _ in range(2)]
l = [[] for _ in range(2)]

for _ in range(n1):
    a, b = map(int, input().split())
    v[0].append(a)
    l[0].append(b)

for _ in range(n2):
    a, b = map(int, input().split())
    v[1].append(a)
    l[1].append(b)

