n, l, r = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
    if l <= a[i] < r:
        print(a[i])
    elif a[i] < l:
        print(l)
    else:
        print(r)
