from math import ceil
n, x, t = map(int, input().split())
ans = int(ceil(n / x)) * t
print(ans)
