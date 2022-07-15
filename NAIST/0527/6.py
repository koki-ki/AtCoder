n = int(input())
k = list(map(int, input().split()))
k_sort = k.copy()
k_sort.sort()
l = [0] * n
ki = list(range(0, n - 1))

for i in range(len(k)):
    for j in range(len(k)):
        if k_sort[i] == k[j]:
            if l[j] == 0:
                l[j] = k[j]
            if l[j + 1] == 0:
                l[j + 1] = k[j]


print(*l)