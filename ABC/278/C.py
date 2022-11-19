n, q = map(int, input().split())

members = set()
n = 0
A = []
B = []
T = []

for _ in range(q):
    t, a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    T.append(t)

S = sorted(list(set(A) | set(B)))
ranking = {x: i + 1 for i, x in enumerate(S)}
A_zaatsu = []
B_zaatsu = []
for a, b in zip(A, B):
    A_zaatsu.append(ranking[a])

    B_zaatsu.append(ranking[b])
ans = []
G = [set() for _ in range(len(S) + 1)]
for i in range(q):
    a, b, t = A_zaatsu[i], B_zaatsu[i], T[i]

    if t == 1:
        if b not in G[a]:
            G[a].add(b)
    if t == 2:
        if b in G[a]:
            G[a].remove(b)
    if t == 3:
        if b in G[a] and a in G[b]:
            ans.append('Yes')
        else:
            ans.append('No')


for a in ans:
    print(a)
