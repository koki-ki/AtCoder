n = int(input())

point = [[0] * 5 for _ in range(10 ** 5 + 1)]
a = [[0] * 5 for _ in range(10 ** 5 + 1)]
# print('a')
# print(a)
tn = 0
for i in range(n):
    # print(i)
    # print(a)
    t_, x_, a_ = map(int, input().split())
    print(t_, x_)
    a[t_][x_] = a_
    tn = max(tn, t_)
ans = 0
for t in range(tn + 1):

    for x in range(5):
        if x == 0:
            point[t + 1][0] = max(point[t][0] + a[t + 1][0],
                                  point[t][1] + a[t + 1][0])
        elif 1 <= x <= 3 and x <= t:
            point[t + 1][x] = max(point[t][x - 1] + a[t + 1][x],
                                  point[t][x] + a[t + 1][x],
                                  point[t][x + 1] + a[t + 1][x])
        elif x == 4 and x <= t:
            point[t + 1][4] = max(point[t][3] + a[t + 1][4],
                                  point[t][4] + a[t + 1][4])
    ans = max(ans, max(point[t]))
    print(point[t])

print(ans)
