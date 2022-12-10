n, t = map(int, input().split())
a = list(map(int, input().split()))
cum = [0] * len(a)
cum[0] = a[0]

for i in range(1, len(a)):
    cum[i] = cum[i - 1] + a[i]
cum.insert(0, 0)
sum = cum[-1]

if t > sum:
    t -= (t // sum) * sum

for i in range(0, n):
    if cum[i] <= t < cum[i + 1]:
        ans1 = i + 1
        ans2 = t - cum[i]

print(ans1, ans2)
