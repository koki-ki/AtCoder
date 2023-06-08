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

n, m = map(int, input().split())
a = list(map(int, input().split()))

checked_prime_factors = set()
candidates = set([i for i in range(1, m + 1)])
for ai in a:
    if ai == 1:
        continue
    ai_prime_factors = factorization_dist(ai).keys()

    for ai_prime_factor in ai_prime_factors:
        if ai_prime_factor in checked_prime_factors:
            break
        checked_prime_factors.add(ai_prime_factor)

        num = 0

        while num <= m:

            if num in candidates:
                candidates.remove(num)
            num += ai_prime_factor


ans = list(candidates)
ans.sort()
num = len(ans)
print(num)
for ai in ans:
    print(ai)