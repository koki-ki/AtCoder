n, m, q = map(int, input().split())
w = [0] * (n + 1)
v = [0] * (n + 1)

for i in range(1, n + 1):
    w[i], v[i] = map(int, input().split())

x = list(map(int, input().split()))
for _ in range(q):
    l, r = map(int, input().split())
