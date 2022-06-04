import math
def lcm(x, y):
    return (x * y) // math.gcd(x, y)

n, a, b = map(int, input().split())
ab = lcm(a, b)
a_ = n // a
b_ = n // b
ab_ = n // ab
a_max = a * a_
b_max = b * b_

def wa(x, x_):
    return (x_ + 1) * x * x_ // 2

ans = (1 + n) * n // 2
ans += wa(ab, ab_) - wa(a, a_) - wa(b, b_)
print(ans)

