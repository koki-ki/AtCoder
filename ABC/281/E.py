n, m, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
cum = [0] * len(a)
cum[0] = a[0]

for i in range(1, len(a)):
    cum[i] = cum[i - 1] + a[i]
cum.insert(0, 0)
sum = cum[-1]
ans = []

for i in range(1, n - m + 2):


