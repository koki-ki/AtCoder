n, k, q = map(int, input().split())
a = [int(input()) for _ in range(q)]

points = [k for _ in range(n)]
for ai in a:
    points[ai - 1] += 1

for point in points:
    if point - q > 0:
        print('Yes')
    else:
        print('No')
