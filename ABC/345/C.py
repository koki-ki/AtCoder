from collections import Counter

s = input()
n = len(s)
count = Counter(s)

ans = (n * n - sum(x * x for x in count.values())) // 2
if max(count.values()) >= 2:
    ans += 1
print(ans)
