n = int(input())
s = [0] + list(map(int, input().split()))
a = [0] * (n + 1)
cum = 0
for k in range(1, n + 1):
    a[k] = s[k] - cum
    cum += a[k]
print(*a[1:])
