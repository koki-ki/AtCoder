from bisect import bisect_left

n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

for i in range(n):
    j = bisect_left(a, a[i] - x)
    j = n - 1 if j == n else j
    if a[i] - a[j] == x:
        print("Yes")
        exit()

print("No")