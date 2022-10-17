from collections import deque
n, q = map(int, input().split())
a = deque(list(map(int, input().split())))
t = []
x = []
y = []
for _ in range(q):
    t_, x_, y_ = map(int, input().split())
    t.append(t_)
    x.append(x_)
    y.append(y_)
for i in range(q):
    if t[i] == 1:
        a[x[i] - 1], a[y[i] - 1] = a[y[i] - 1], a[x[i] - 1]
    elif t[i] == 2:
        a.rotate()
    elif t[i] == 3:
        print(a[x[i] - 1])
