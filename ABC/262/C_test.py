n = int(input())
INF = 10 ** 9
a = [INF]
a_ = list(map(int, input().split()))
a.extend(a_)
ans = 0
z = [INF]


for i in range(1, n ):
    for j in range(i + 1, n + 1):
        if min(a[i], a[j]) == i and max(a[i], a[j]) == j:
            # print(i, j, a[i], a[j])
            ans += 1