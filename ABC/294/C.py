from bisect import bisect_left

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = a + b
c.sort()
ans = []
for i in range(n):
    ind = bisect_left(c, a[i])
    ans.append(ind + 1)
print(*ans)
ans = []
for i in range(m):
    ind = bisect_left(c, b[i])
    ans.append(ind + 1)
print(*ans)
