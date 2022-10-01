n, k, x = map(int, input().split())
a = list(map(int, input().split()))
last = len(a) - 1

for i in range(n):
    if a[i] // x <= k:
        k -= a[i] // x
        a[i] -= (a[i] // x) * x
    else:
        a[i] -= k * x
        k = 0

a.sort(reverse=True)

for i in range(n):
    if 1 <= k:
        a[i] = 0
        k -= 1
    else:
        break

ans = sum(a)
print(ans)


