n = int(input())
a = list(map(int, input().split()))
a.sort()
a_min = a[0]
a_max = a[-1]
a_origin = list(range(a_min, a_max + 1))

for i in range(n):
    if a[i] != a_origin[i]:
        print(a_origin[i])
        exit()
