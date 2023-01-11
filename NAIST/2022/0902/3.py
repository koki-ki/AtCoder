from math import ceil
x, a, d, n = map(int, input().split())


def A(n):
    return a + (n - 1) * d


a0 = A(0)
a1 = A(1)
aN = A(n)
aN1 = A(n + 1)

if d == 0:
    print(abs(x - a))
    exit()
if a0 <= x <= aN1 or aN1 <= x <= a0:
    l = ceil((x - a) / d)
    al = A(l)
    al1 = A(l + 1)
    ans = min(abs(x - al), abs(x - al1))
else:
    ans = min(abs(a1 - x), abs(aN - x))
print(ans)
