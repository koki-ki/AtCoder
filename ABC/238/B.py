n = int(input())
a = list(map(int, input().split()))
cut = [0, 360]
now = 0
for ai in a:
    cut.append((now + ai) % 360)
    now += ai
    now %= 360
cut.sort()
ans = 0
for i in range(1, n + 2):
    ans = max(ans, cut[i] - cut[i - 1])
print(ans)