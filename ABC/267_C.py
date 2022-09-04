n, m = map(int, input().split())
a = [-10**18] + list(map(int, input().split()))
ruiseki = [0] * (n + 1)

wa = [0] * (n - m + 2)
wa[0] = - 10 ** 18
for i in range(1, n + 1):
    ruiseki[i] = ruiseki[i - 1] + a[i]
for i in range(1, m + 1):
    wa[1] += i * a[i]

for i in range(2, n - m + 2):
    wa[i] = wa[i - 1] + m * a[i + m - 1] - \
        (ruiseki[i + m - 2] - ruiseki[i - 2])
print(max(wa))
