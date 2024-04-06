def calc_distance_squared(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2


n = int(input())
x, y = [None for _ in range(n)], [None for _ in range(n)]

for i in range(n):
    x[i], y[i] = map(int, input().split())


for i in range(n):
    tmp = 0
    max_distance = 0
    for j in range(n):
        tmp_distance = calc_distance_squared((x[i], y[i]), (x[j], y[j]))
        if tmp_distance > max_distance:
            max_distance = tmp_distance
            tmp = j
    print(tmp + 1)
