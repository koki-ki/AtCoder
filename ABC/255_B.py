from math import sqrt
n, k = map(int, input().split())
a = list(map(int, input().split()))[::-1]
x = [0] * (n + 1)
y = [0] * (n + 1)

for i in range(1, n + 1):
    x[i], y[i] = map(int, input().split())

ans = 0
for i in range(1, n + 1):
    d = float('inf')
    for j in a:
        d = min(d, sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2))
    ans = max(ans, d)
print(ans)
