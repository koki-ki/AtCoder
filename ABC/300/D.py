from collections import defaultdict
from math import ceil, floor

def eratosthenes(n):
    isPrimes = [True] * (n+1)

    isPrimes[0], isPrimes[1] = False, False

    for i in range(2, int(n**0.5)+1):
        if isPrimes[i]:
            for j in range(2*i, n+1, i):
                isPrimes[j] = False
    return [i for i in range(2, n+1) if isPrimes[i]]

n = int(input())
amax = ceil((10 ** 12) ** 0.2)
list_prime = eratosthenes(10 ** 6)
set_prime = set(list_prime)

ld = len(list_prime)

ans = 0

for i in range(ld - 2):
    a = list_prime[i]
    if a > amax:
        break
    for j in range(i + 1, ld - 1):
        b = list_prime[j]
        aab = a * a * b
        if n < aab:
            break
        for k in range(j + 1, ld):
            c = list_prime[k]
            # print(i, j, k)
            aabcc = aab * c * c
            if aabcc <= n:
                ans += 1
            else:
                break

print(ans)
# print(nums)