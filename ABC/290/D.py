from math import gcd

t = int(input())
last = 0
N = []
D = []
K = []
for _ in range(t):
    ni, di, ki = map(int, input().split())
    N.append(ni)
    D.append(di)
    K.append(ki)

for n, d, k in zip(N, D, K):
    a = n / gcd(n, d)
    k -= 1
    ans = d * k % n + k // a
    ans = int(ans)
    print(ans)