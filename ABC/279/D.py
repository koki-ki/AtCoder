from math import sqrt
a, b = map(int, input().split())


def f(n):
    return a / sqrt(n + 1) + b * n


l = 0
r = a / b
while r - l > 2:
    m1 = (l * 2 + r) / 3
    m2 = (l + r * 2) / 3
    if f(m1) > f(m2):
        l = m1
    else:
        r = m2

ans = a
for i in range(int(l), int(r) + 1):
    ans = min(ans, f(i))
print(ans)
