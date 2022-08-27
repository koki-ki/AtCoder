n = int(input())
t, x, a = [], [], []
point = [[0] * 5 for _ in range(n)]
# for _ in range(n):
#     t_, x_, a_ = map(int, input().split())
#     t.append(t_)
#     x.append(x_)
#     a.append(a_)
for _ in range(n):
    t_, x_, a_ = map(int, input().split())
    point[t_, x_] = a_

now = 0
