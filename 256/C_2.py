HW = list(map(int, input().split()))
h = HW[:3]
w = HW[3:]
ans = 0

for i in range(1, h[0] - 1):
    for j in range(1, h[0] - i):
        m13 = h[0] - i - j
        if m13 <= 0:
            break
        for k in range(1, w[0] - i):
            m31 = w[0] - i - k
            for l in range(1, min(h[1] - k, w[1] - j)):
                m23 = h[1] - k - l
                m32 = w[1] - j - l
                if m32 <= 0 or m23 <= 0:
                    break
                m33 = w[2] - m13 - m23
                if m33 == h[2] - m31 - m32 and m33 >= 1:
                    ans += 1

print(ans)