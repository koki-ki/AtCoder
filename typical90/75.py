from collections import defaultdict
from math import ceil
def factorization_dist(n):
    dist = defaultdict(int)
    '''
    from collections import defaultdict
    '''
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            dist[i] += cnt
    if temp != 1:
        dist[temp] = 1
    if len(dist.keys()) == 0:
        dist[n] = 1
    return dist

n = int(input())
num_primes = sum(factorization_dist(n).values())
ans = 0
while num_primes != 1:
    ans += 1
    num_primes = ceil(num_primes / 2)
print(ans)
