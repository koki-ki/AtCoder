from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
q = int(input())
add = defaultdict(int)
base = 0
for i, a_ in enumerate(a):
    add[i] = a_
ans = []

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        base = x
        add = defaultdict(int)
    if query[0] == 2:
        i, x = query[1:]
        i -= 1
        add[i] += x
    if query[0] == 3:
        i = query[1]
        i -= 1
        ans.append(base + add[i])

for a in ans:
    print(a)
