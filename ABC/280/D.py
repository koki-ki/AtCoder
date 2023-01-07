from collections import defaultdict
k = int(input())


def factorization_dist(n):
    '''
    from collections import defaultdict
    '''
    dist = defaultdict(int)
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


d = factorization_dist(k)
print(d)
