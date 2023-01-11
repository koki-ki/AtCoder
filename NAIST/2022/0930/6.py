from math import gcd
from collections import Counter
n, m = map(int, input().split())
A = list(map(int, input().split()))
factors = set()


def prime_factorize(N):
    primes = []
    for i in range(2, N + 1):
        primes.append(i)
        for p in range(2, i):
            if i % p == 0:
                primes.remove(i)
                break
    return primes


for a in A:
    a = Counter(prime_factorize(a))
    a = list(a.keys())
    factors.update(a)


souseki = 1
for f in factors:
    souseki *= f
ans = []
for k in range(1, m + 1):
    if gcd(k, souseki) == 1:
        ans.append(k)


print(len(ans))
for a in ans:
    print(a)
