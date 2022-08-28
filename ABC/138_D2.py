from collections import deque
n, q = map(int, input().split())

A = [[] for _ in range(n)]
c = [0] * n
p, x = [], []

for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    A[a].append(b)
    A[b].append(a)

for i in range(q):
    p_, x_ = map(int, input().split())
    p.append(p_)
    x.append(x_)

for i in range(q):
    tasu = [] # 足されるノード
    work_stack = [p[i]]

    while work_stack:
        here = work_stack.pop()
        for i, node in enumerate(A[here]):
            if node == 0: continue
            if i not in tasu:
                work_stack.append(i)
                tasu.append(i)

    for j in tasu:
        c[j] += x[i]

print(*c)
