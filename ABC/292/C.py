from collections import defaultdict

def factorization_dist(n):
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

n = int(input())
ans = 0
for i in range(1, n // 2 + 1):
    tmp = 1
    dist1 = factorization_dist(i)
    dist2 = factorization_dist(n - i)
    ############
    # print(i)
    # print(dist1)
    # print(dist2)
    ############
    for key in dist1.keys():
        if key == 1:
            continue
        tmp *= dist1[key] + 1
    for key in dist2.keys():
        if key == 1:
            continue
        tmp *= dist2[key] + 1
    if i != n - i:
        ans += tmp * 2
    else:
        ans += tmp

print(ans)