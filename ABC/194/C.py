from collections import Counter
N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)

ans = 0
for x in range(-200, 201):
    for y in range(x + 1, 201):
        ans += cnt[x] * cnt[y] * (x - y) ** 2

print(ans)
