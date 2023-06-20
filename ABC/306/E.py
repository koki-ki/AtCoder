def f(a):
    b = sorted(a)
    return sum(b[:k])

n, k, q = map(int, input().split())
a = [0 for _ in range(n)]

for _ in range(q):
    x, y = map(int, input().split())
    a[x - 1] = y
