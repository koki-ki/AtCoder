from math import ceil, sqrt
n = int(input())
ans = ceil((-1 + sqrt(1 + 8 * n)) / 2)
print(ans)
