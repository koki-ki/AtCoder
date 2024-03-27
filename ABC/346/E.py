h, w, m = map(int, input().split())
t, a, x = [], [], []

for _ in range(m):
    ti, ai, xi = map(int, input().split())
    t.append(ti)
    a.append(ai)
    x.append(xi)

f = [False for _ in range(h)]
g = [False for _ in range(w)]
X = 200010
cnt = [0 for _ in range(X)]

for i in range(m - 1, -1, -1):

