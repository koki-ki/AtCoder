from math import ceil, floor

x, k, d = map(int, input().split())
x = abs(x)

if x - k * d >= 0:
    ans = x - k * d
else:
    ans = min(
        abs(x - ceil(x / d) * d + d * (k % 2 + 1)),
        abs(x - floor(x / d) * d + d * (k % 2 + 1)),
        abs(x - ceil(x / d) * d - d * (k % 2 + 1)),
        abs(x - floor(x / d) * d - d * (k % 2 + 1))
    )

print(ans)
