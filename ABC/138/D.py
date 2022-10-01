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
    tasu = []
    work_stack = [p[i]]

    while work_stack:
        here = work_stack.pop()
        if len(A[i]) == 0:
            continue
        for j in range(len(A[i])):
            tasu.append(A[i][j])
            work_stack.append(A[i][j])

    for j in A[i][j]:
        p[j] += x[i]

for i in range(n):
    print(c[i])
