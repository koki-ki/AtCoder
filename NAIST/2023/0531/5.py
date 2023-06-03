from bisect import bisect_left as bl

n = int(input())
a = list(map(int, input().split()))

b = [0 for _ in range(n)]
b[0] = a[0]
for i in range(1, n):
    b[i] = b[i - 1] + a[i]

sum_a = sum(a)
half_a = sum_a / 2

i = bl(b, half_a)
if i == n - 1:
    i -= 1

leftside = b[i]
rightside = b[-1] - b[i]

ans = abs(half_a - leftside) + abs(half_a - rightside)
ans = int(ans)

print(ans)