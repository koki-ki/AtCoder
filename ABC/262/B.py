n, m = map(int, input().split())
u, v = [], []
for i in range(m):
    u_, v_ = map(int, input().split())
    u.append(u_ - 1)
    v.append(v_ - 1)

ans = 0
for a in range(n - 2):
    for b in range(a + 1, n - 1):
        # plan A
        # for c in range(b + 1, n):
        #     cnt = 0
        #     for i in range(m):
        #         if (u[i] == a and v[i] == b) or (u[i] == b and v[i] == a):
        #             cnt += 1
        #         if (u[i] == b and v[i] ==c ) or (u[i] == c and v[i] == b):
        #             cnt += 1
        #         if (u[i] == c and v[i] == a) or (u[i] == a and v[i] == c):
        #             cnt += 1
        #     if cnt == 3:
        #         ans += 1

        # plan B
        for i in range(m):
            if (u[i] == a and v[i] == b) or (u[i] == b and v[i] == a):


print(ans)