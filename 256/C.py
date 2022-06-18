HW = list(map(int, input().split()))
h = HW[:3]
w = HW[3:]
ans = 0

for i in range(1, h[0] - 1):
    m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    m[0][0] = i

    for j in range(1, h[0] - 1 - m[0][0]):
        m[0][1] = j
        if m[0][0] + m[0][1] > h[0]:
            continue
        m[0][2] = h[0] - m[0][0] - m[0][1]

        for k in range(1, w[0] - m[0][0]):
            m[1][0] = k

            for l in range(1, min(h[1] - m[1][0], w[1] - m[0][1])):
                m[1][1] = l
                if m[1][0] + m[1][1] > h[1] or m[0][1] + m[1][1] > w[1]:
                    continue
                m[1][2] = h[1] - m[1][0] - m[1][1]
                m[2][1] = w[1] - m[0][1] - m[1][1]
                m[2][2] = w[2] - m[0][2] - m[1][2]
                if m[2][2] <= 0:
                    continue
                ans += 1

print(ans)