n, p, q, r, s = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = a.copy()
for i in range(q - p + 1):
    b[p + i], b[r + i] = a[r + i], a[p + i]

print(*b[1:])

# a[p: q + 1], a[r, s + 1] = a[r, s + 1], a[p: q + 1]
# print(*a[1:])
