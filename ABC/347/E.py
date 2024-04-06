n, q = map(int, input().split())
x = list(map(int, input().split()))
a = [0 for _ in range(n + 1)]
s = set()

b = [[] for _ in range(n + 1)]


for i, xi in enumerate(x):
    if xi in s:
        s.remove(xi)

    else:
        s.add(xi)


print(*a[1:])
