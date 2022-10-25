from math import gcd


def my_lcm(a, b):
    return a * b // gcd(a, b)


a, b = map(int, input().split())
ans = my_lcm(a, b)
if ans > 10 ** 18:
    print('Large')
else:
    print(ans)
