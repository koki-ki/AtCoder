from math import gcd


def lcm(x, y):
    return (x * y) // gcd(x, y)


n = int(input())
t = []
for _ in range(n):
    t.append(int(input()))
ans = t[0]
for i in range(1, n):
    ans = lcm(ans, t[i])
print(ans)
