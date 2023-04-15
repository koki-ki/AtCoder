from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
socks = defaultdict(int)

for s in a:
    socks[s] += 1

cnt = 0
for n in socks.values():
    cnt += n // 2

print(cnt)
