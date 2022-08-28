n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
anss = []

for _ in range(q):
    x = int(input())
    left = 0
    right = n - 1
    center = (left + right) // 2
    while True:
        if a[center] >= x:
            print(n - x)
            break
