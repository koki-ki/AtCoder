n = int(input())
p = list(map(int, input().split()))
cnt = [0] * n
for i in range(n):
    j = (p[i] - 1 - i - 1 + n) % n
    cnt[j] += 1
    cnt[(j + 1) % n] += 1
    cnt[(j + 2) % n] += 1
ans = max(cnt)
print(ans)
