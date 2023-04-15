from collections import defaultdict

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

k = int(input())
primes = factorization_dist(k)
N = []

for prime in primes:

