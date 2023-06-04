from collections import defaultdict
from bisect import bisect_left as bl

w, h = map(int, input().split())
n = int(input())

p = []
q = []
for _ in range(n):
    pi, qi = map(int, input().split())
    p.append(pi)
    q.append(qi)

cnt = defaultdict(int)


A = int(input())
a = [0] + list(map(int, input().split()))
B = int(input())
b = [0] + list(map(int, input().split()))

for pi, qi in zip(p, q):
    ai = bl(a, pi)
    bi = bl(b, qi)
    cnt[(ai, bi)] += 1

m = min(cnt.values())
M = max(cnt.values())

if len(cnt.keys()) < (A + 1) * (B + 1):
    m = 0

print(m, M)

