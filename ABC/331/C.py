from copy import deepcopy
from bisect import bisect_right

n = int(input())
a = list(map(int, input().split()))
a_sorted = sorted(deepcopy(a))

acc_a_sorted = [0] * n
acc_a_sorted[0] = a_sorted[0]

for i in range(1, n):
    acc_a_sorted[i] = acc_a_sorted[i - 1] + a_sorted[i]

for i in range(n):
    idx = bisect_right(a_sorted, a[i])
    if idx == n:
        print(0, end=" ")
    else:
        ans = acc_a_sorted[n - 1] - acc_a_sorted[idx - 1]
        print(ans, end=" ")

print()
