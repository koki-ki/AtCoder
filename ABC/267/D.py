n, m = map(int, input().split())
INF = 10 ** 18
a = [-INF] + list(map(int, input().split()))
wa = [-INF] * (n + 1)
nums = [0] * (4 * 10 ** 5 + 1)

for i, a_ in enumerate(a[1:], start=1):
    nums[a_] += 1

Min = INF
Min_i = 1
for i in range(1, m + 1):
    wa[m] += i * a[i]
    if Min <= a[i]:
        nums[Min] -= 1
        nums[a[i]] += 1
        Min_i = i

for i in range(m + 1, n + 1):
    if a[i] > Min_
