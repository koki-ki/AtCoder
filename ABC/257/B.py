n, k, q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))

for i in range(q):
    if a[l[i] - 1] == n or l[i] + 1 == n:
        continue

    if a[l[i] - 1] + 1 == n:
        a[l[i] - 1] += 1
        continue

    if a[l[i]] != a[l[i] - 1] + 1:
        a[l[i] - 1] += 1

print(*a)