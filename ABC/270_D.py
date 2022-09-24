n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
i = len(a) - 1
taka = 0
aoki = 0
cnt = 0

while n > 0:
    if a[i] > n:
        i -= 1
        continue

    if cnt % 2 == 0:
        taka += a[i]
        n -= a[i]
    else:
        aoki += a[i]
        n -= a[i]
    cnt += 1

print(taka)
